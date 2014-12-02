from ..dynamic_fields_block import DynamicFields
from nio.util.support.block_test_case import NIOBlockTestCase
from nio.common.signal.base import Signal


class DummySignal(Signal):
    
    def __init__(self, val):
        super().__init__()
        self.val = val


class TestDynamicFields(NIOBlockTestCase):
    
    def setUp(self):
        super().setUp()
        self.last_notified = []
    
    def signals_notified(self, signals):
        self.last_notified = signals

    def test_pass(self):
        signals = [DummySignal("a banana!")]
        attrs = signals[0].__dict__
        blk = DynamicFields()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals(signals)
        self.assertDictEqual(attrs, self.last_notified[0].__dict__)
    
    def test_add_field(self):
        signals = [DummySignal("a banana!")]
        blk = DynamicFields()
        config = {
            "fields": [{
                "title": "greeting",
                "formula": "I am {{$val}}"
            }]
        }
        self.configure_block(blk, config)
        blk.start()
        blk.process_signals(signals)
        sig = self.last_notified[0]
        self.assertTrue(hasattr(sig, 'greeting'))
        self.assertTrue(hasattr(sig, 'val'))
        self.assertEqual(sig.greeting, "I am a banana!")

    def test_exclude(self):
        signals = [DummySignal("stumped...")]
        blk = DynamicFields()
        config = {
            "exclude": True,
            "fields": [{
                "title": "greeting",
                "formula": "I am {{$val}}"
            }]
        }
        self.configure_block(blk, config)
        blk.start()
        blk.process_signals(signals)
        sig = self.last_notified[0]
        self.assertTrue(hasattr(sig, 'greeting'))
        self.assertFalse(hasattr(sig, 'val'))
        self.assertEqual(sig.greeting, "I am stumped...")

    def test_bogus_field(self):
        signals = [DummySignal("you won't see me")]
        blk = DynamicFields()
        self.configure_block(blk, {
            "exclude": True,
            "fields": [{
                "title": "greeting",
                "formula": "I am {{dict($val)}}"
            }]
        })
        blk.start()
        blk.process_signals(signals)
        sig = self.last_notified[0]
        self.assertTrue(hasattr(sig, 'greeting'))
        self.assertIsNone(sig.greeting)