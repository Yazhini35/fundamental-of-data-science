import numpy as np
student_scores = np.array([
    [85, 78, 92, 88],
    [76, 85, 90, 80],
    [90, 88, 84, 92],
    [70, 75, 80, 85]
])
average_scores = np.mean(student_scores, axis=0)
subjects = ['Math', 'Science', 'English', 'History']
highest_avg_score_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_score_index]
print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", highest_avg_subject)
