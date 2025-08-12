class chatbot:
    def __init__(self, name):
        self.name = name
        # Variable to store the latest question asked by the user
        self.question = None
        # Simple database of known questions and answers
        self.DB = {
            "what is your name": "my name is chatbot",
            "what is my name": self.name,
        }

    def extractNumber(self):
        """
        Extracts all numbers from the current question (string).
        Returns a list of integers found in the question.
        Example: "add 5 and 10" → [5, 10]
        """
        finished = None
        nums = []
        num = ""
        # Add a space at the end to ensure last number is processed
        for i in self.question + " ":
            if i.isnumeric():
                num += i
                finished = 1
            elif finished:
                nums.append(int(num))
                finished = 0
                num = ""
        return nums

    def numiercOUTPUT(self, op):
        """
        Builds a string showing the calculation process.
        Example: op = "+" and nums = [5, 10] → "5 + 10 ="
        """
        out = ""
        for num in self.extractNumber():
            out += f" {num} {op}"
        out = out.removesuffix(f"{op}")  # Remove the last operator
        out += "="
        return out[1:]  # Remove leading space

    def How(self):
        """
        If the chatbot doesn't know the answer,
        ask the user to teach it and store it in the database.
        """
        print(
            f"CHATBOT: sorry {self.name} it seems that I don't know how to answer. Can you help me learn?"
        )
        print("CHATBOT: enter the right answer: ")
        answer = input()
        self.DB[self.question] = answer  # Store new Q&A pair

    def ask(self):
        """
        Ask the user for a question.
        Returns 1 if user typed 'exit' to end chat, else 0.
        """
        exit = 0
        print(f"CHATBOT: Hi {self.name}! I am chatbot, how can I help you?")
        print("you: ")
        qu = input()
        self.question = qu
        if qu == "exit":
            exit = 1
        return exit

    def answer(self):
        """
        Processes the current question and prints the answer.
        Supports:
            - Database lookup
            - Addition ("add")
            - Subtraction ("sup")
            - Multiplication ("multiply")
            - Division ("divied")
            - Power ("power")
            - Modulus ("modulos")
        If unknown, calls self.How() to learn.
        """
        # Check if question exists in database
        if self.DB.get(self.question) is not None:
            print(self.DB.get(self.question))

        elif "add" in self.question:
            nums = self.extractNumber()
            if len(nums) > 1:
                print(f"CHATBOT: {self.numiercOUTPUT('+')} {sum(nums)}")
            else:
                pass  # Not enough numbers provided

        elif "sup" in self.question:
            nums = self.extractNumber()
            ans = nums[0]
            for i in nums[1:]:
                ans -= i
            if len(nums) > 1:
                print(f"CHATBOT: {self.numiercOUTPUT('-')} {ans}")
            else:
                pass

        elif "multiply" in self.question:
            ans = 1
            nums = self.extractNumber()
            for i in nums:
                ans *= i
            if len(nums) > 1:
                print(f"CHATBOT: {self.numiercOUTPUT('*')} {ans}")
            else:
                self.How()

        elif "divied" in self.question:
            nums = self.extractNumber()
            if len(nums) > 1:
                ans = nums[0]
                for i in nums[1:]:
                    ans /= i
                print(f"CHATBOT: {self.numiercOUTPUT('/')} {ans}")
            else:
                self.How()

        elif "power" in self.question:
            nums = self.extractNumber()
            if len(nums) > 1:
                print(f"CHATBOT: {self.numiercOUTPUT('**')} {nums[0]**nums[1]}")
            else:
                self.How()

        elif "modulos" in self.question:
            nums = self.extractNumber()
            if len(nums) > 1:
                print(f"CHATBOT: {self.numiercOUTPUT('%')} {nums[0] % nums[1]}")
            else:
                self.How()

        else:
            self.How()


if __name__ == "__main__":
    hi = chatbot(input("Enter your name: "))
    while True:
        exit = hi.ask()
        if exit:
            break
        hi.answer()
