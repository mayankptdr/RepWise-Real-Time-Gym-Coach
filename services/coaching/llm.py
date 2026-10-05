from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, gemini_client):
        self.client = gemini_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):

        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        history_text = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in self.history[-10:]]
        )

        full_prompt = f"""
            System Instructions:
            {self.system_prompt}

            Conversation History:
            {history_text}

            User Input:
            {prompt}
            """

        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=full_prompt
        )


        text = response.text.strip()

        self.history.append({
            "role": "assistant",
            "content": text
        })


        

        return text

