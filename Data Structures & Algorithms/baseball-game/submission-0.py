class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []
        for i in range(0, len(operations)):
            if operations[i] == '+':
                ops.append(ops[-1] + ops[-2])
            elif operations[i] == 'C':
                ops.pop()
            elif operations[i] == 'D':
                ops.append(ops[-1] * 2)
            else:
                ops.append(int(operations[i]))
        return sum(ops)