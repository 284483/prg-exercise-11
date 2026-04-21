class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score=self.get_by_index(index)
        if score<50:
            return "F"
        elif score<60:
            return "E"
        elif score<70:
            return "D"
        elif score<80:
            return "B"
        elif score<90:
            return "C"
        else:
            return "A"

    def find(self, find_score):
        zoznam=[]
        # for i in range(len(self.scores)):
        #     if self.scores[i]==find_score:
        #         zoznam.append(i)
        for i in self.scores:
            if i == find_score:
                zoznam.append(self.scores.index(i))
        return zoznam

    def get_sorted(self):
        scores=self.scores.copy()
        n = len(scores)
        for i in range(n):
            for j in range(0, n - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores



results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
def main():
    #
    # print(results.count())  # 9
    # print(results.scores)
    # print(results.get_grade(2))
    # print(results.find(85))
    # print(results.get_sorted())
    # print(results.scores)
    pocet_ziakov=results.count()
    for i in range(pocet_ziakov):
        body = results.get_by_index(i)  # 91
        znamka=results.get_grade(i)
        print(f"Student {i+1}: {body} points - {znamka}")
if __name__ == "__main__":
    main()