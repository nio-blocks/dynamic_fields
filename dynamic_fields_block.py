from nio.common.block.base import Block
from nio.common.signal.base import Signal
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties.list import ListProperty
from nio.metadata.properties.expression import ExpressionProperty
from nio.metadata.properties.string import StringProperty
from nio.metadata.properties.holder import PropertyHolder
from nio.metadata.properties.bool import BoolProperty


class SignalField(PropertyHolder):
    title = StringProperty(default='')
    formula = ExpressionProperty(default='')


@Discoverable(DiscoverableType.block)
class DynamicFields(Block):
    
    """ Dynamic Fields block.

    A NIO block for enriching signals dynamically.

    By default, the dynamic fields block adds attributes to
    existing signals as specified. If the 'exclude' flag is
    set, the block instantiates new (generic) signals and
    passes them along with *only* the specified fields.

    """

    fields = ListProperty(SignalField, title='Fields')
    exclude = BoolProperty(default=False, title='Exclude existing fields?')

    def process_signals(self, signals):
        """ Overridden from the block interface.

        """
        fresh_signals = []

        for signal in signals:

            # if we are including only the specified fields, create
            # a new, empty signal object
            tmp = Signal() if self.exclude else signal

            # iterate over the specified fields, evaluating the formula
            # in the context of the original signal
            for field in self.fields:
                try:
                    value = field.formula(signal)
                except Exception as e:
                    value = None
                    self._logger.error(
                        "Dynamic field {0} evaluation failed: {0}: {1}".format(
                            type(e).__name__, str(e))
                    )
                    
                setattr(tmp, field.title, value)

            # only rebuild the signal list if we're using new objects
            if self.exclude:
                fresh_signals.append(tmp)

        if self.exclude:
            signals = fresh_signals

        self.notify_signals(signals)
