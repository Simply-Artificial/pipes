from transformers import Conversation


class BetterConversation(Conversation):
    def to_dict(self):
        return {
            "uuid": self.uuid,
            "past_user_inputs": self.past_user_inputs,
            "generated_responses": self.generated_responses,
            "new_user_input": self.new_user_input,
        }

    def from_dict(self, d: dict):
        self.uuid = d["uuid"]
        self.past_user_inputs = d["past_user_inputs"]
        self.generated_responses = d["generated_responses"]
        self.new_user_input = d["new_user_input"]
