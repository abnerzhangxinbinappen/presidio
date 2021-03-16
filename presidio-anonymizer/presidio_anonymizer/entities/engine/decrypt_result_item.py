""""Result item from the /decrypt method."""
from presidio_anonymizer.entities.engine.engine_result_item import EngineResultItem
from presidio_anonymizer.entities.manipulator.manipulated_result_entity import \
    ManipulatedEntity


class DecryptResultItem(EngineResultItem):
    """Information about the decrypted entity."""

    def __init__(
            self,
            start: int,
            end: int,
            decrypted_text: str,
    ):
        """Create DecryptedEntity.

        :param start: start index in the decrypted text.
        :param end: end index in the decrypted text.
        :param decrypted_text: the PII decrypted text.
        """
        self.start = start
        self.end = end
        self.decrypted_text = decrypted_text

    @classmethod
    def from_manipulated_entity(cls,
                                manipulated_entity: ManipulatedEntity) -> 'DecryptResultItem':
        return cls(manipulated_entity.start, manipulated_entity.end,
                   manipulated_entity.manipulated_text)
