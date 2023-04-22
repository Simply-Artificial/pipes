from transformers import Conversation

__all__ = ["BetterConversation"]


class BetterConversation(Conversation):
    def to_dict(self) -> dict:
        return {
            "conversation_id": self.uuid,
            "past_user_inputs": self.past_user_inputs,
            "generated_responses": self.generated_responses,
        }
