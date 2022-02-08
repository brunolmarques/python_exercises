from operator import itemgetter

def round_scores(student_scores):
    """
    return a new list with all the scores converted to ints. The order of the scores in the resulting list is not important.
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return [round(x) for x in student_scores]


def count_failed_students(student_scores):
    """
    count up the number of students who don't have passing scores and return that count as an integer.
    A student needs a score greater than 40 to achieve a passing grade on the exam.
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    return len([x for x in student_scores if x <= 40])


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    return [x for x in student_scores if x >= threshold]


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """

    return [x for x in range(41, highest, (highest - 40) // 4)]


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    l1 = sorted(list(zip(student_names, student_scores)), key= itemgetter(1), reverse= True)

    return ["{}. {}: {}".format(i+1, x[0], x[1]) for i, x in enumerate(l1)]


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    l1 = [[x[0], x[1]] for x in student_info if x[1] == 100]

    if len(l1) == 0:
        return []
    else:
        return l1[0]
