from nio.block.base import Block
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from nio.properties.list import ListProperty
from nio.properties import Property
from nio.properties.string import StringProperty
from nio.properties.holder import PropertyHolder
from nio.properties.bool import BoolProperty


class SignalField(PropertyHolder):
    title = Property(default='')
    formula = Property(default='')


@discoverable
class DynamicFields(Block):

    """ Dynamic Fields block.

    A NIO block for enriching signals dynamically.

    By default, the dynamic fields block adds attributes to
    existing signals as specified. If the 'exclude' flag is
    set, the block instantiates new (generic) signals and
    passes them along with *only* the specified fields.

    """

    fields = ListProperty(SignalField, title='Fields', default=[])
    exclude = BoolProperty(default=False, title='Exclude existing fields?')

    def process_signals(self, signals):
        """ Overridden from the block interface.

        """
        fresh_signals = []

        for signal in signals:

            # if we are including only the specified fields, create
            # a new, empty signal object
            tmp = Signal() if self.exclude() else signal

            # iterate over the specified fields, evaluating the formula
            # in the context of the original signal
            for field in self.fields():
                value = field.formula(signal)
                title = field.title(signal)
                setattr(tmp, title, value)

            # only rebuild the signal list if we're using new objects
            if self.exclude:
                fresh_signals.append(tmp)

        if self.exclude():
            signals = fresh_signals

        self.notify_signals(signals)
