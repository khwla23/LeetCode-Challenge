class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation == "--X":
                x = x - 1
            if operation == "X--":
                x = x - 1

            if operation == "++X":
                x = x+1

            if operation == "X++":
                x = x+1
        return x