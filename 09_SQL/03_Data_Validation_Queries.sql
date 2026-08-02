USE StudentPerformanceAnalytics;
GO

--- 01. Check for NULL Values
--- Students
SELECT *
FROM students
WHERE student_id IS NULL OR name IS NULL;

--- Scores
SELECT *
FROM scores
WHERE student_id IS NULL OR test_id IS NULL OR percentage IS NULL;

--- Tests
SELECT *
FROM tests
WHERE test_id IS NULL OR subject IS NULL;

--- Question Bank
SELECT *
FROM question_bank
WHERE question_id IS NULL OR question_text IS NULL;

--- 02. Detect Duplicate Student IDs
SELECT
student_id,
COUNT(*) AS DuplicateCount
FROM students
GROUP BY student_id
HAVING COUNT(*) > 1;

--- 03. Detect Duplicate Test IDs
SELECT
test_id,
COUNT(*) AS DuplicateCount
FROM tests
GROUP BY test_id
HAVING COUNT(*) > 1;

--- 04. Detect Duplicate Question IDs
SELECT
question_id,
COUNT(*) AS DuplicateCount
FROM question_bank
GROUP BY question_id
HAVING COUNT(*) > 1;

--- 05. Verify Percentage Range (0–100)
SELECT *
FROM scores
WHERE percentage < 0 OR percentage > 100;

--- 06. Verify Marks Obtained ≤ Maximum Marks
SELECT *
FROM scores
WHERE marks_obtained > max_marks;

--- 07. Verify Correct Answers ≤ Total Questions
SELECT *
FROM scores
WHERE correct_answers > total_questions;

--- 08. Verify Wrong Answers are Valid
SELECT *
FROM scores
WHERE wrong_answers < 0;

--- 09. Verify Grades are Valid
SELECT DISTINCT grade
FROM scores;

--- 10. Verify Pass/Fail Values
SELECT DISTINCT pass_fail
FROM scores;

--- 11. Students Without Test Records
SELECT
s.student_id,
s.name
FROM students s
LEFT JOIN scores sc
ON s.student_id = sc.student_id
WHERE sc.student_id IS NULL;

--- 12. Tests Without Scores
SELECT
t.test_id
FROM tests t
LEFT JOIN scores s
ON t.test_id = s.test_id
WHERE s.test_id IS NULL;

--- 13. Responses with Invalid Student IDs
SELECT *
FROM responses
WHERE student_id NOT IN
(
SELECT student_id
FROM students);

--- 14. Responses with Invalid Test IDs
SELECT *
FROM responses
WHERE test_id NOT IN
(
SELECT test_id
FROM tests);

--- 15. Responses with Invalid Question IDs
SELECT *
FROM responses
WHERE question_id NOT IN
(
SELECT question_id
FROM question_bank);

--- 16. Validate Foreign Key Consistency (Scores → Students)
SELECT
sc.student_id
FROM scores sc
LEFT JOIN students s
ON sc.student_id = s.student_id
WHERE s.student_id IS NULL;

--- 17. Validate Foreign Key Consistency (Scores → Tests)
SELECT
sc.test_id
FROM scores sc
LEFT JOIN tests t
ON sc.test_id = t.test_id
WHERE t.test_id IS NULL;

--- 18. Check Average Percentage Range
SELECT *
FROM student_progress
WHERE avg_percentage < 0 OR avg_percentage > 100;

--- 19. Check Risk Levels
SELECT DISTINCT risk_level
FROM student_risk_report;

--- 20. Validate Accuracy Rate
SELECT *
FROM chapter_analytics
WHERE accuracy_rate < 0 OR accuracy_rate > 100;

--- 21. Validate Question Accuracy
SELECT *
FROM question_analytics
WHERE accuracy_rate < 0 OR accuracy_rate > 100;

--- 22. Verify Total Questions > 0
SELECT *
FROM scores
WHERE total_questions <= 0;

--- 23. Verify Maximum Marks > 0
SELECT *
FROM tests
WHERE max_marks <= 0 OR max_marks > 80;

--- 24. Summary Validation Counts
SELECT
    (SELECT COUNT(*) FROM students) AS TotalStudents,
    (SELECT COUNT(*) FROM tests) AS TotalTests,
    (SELECT COUNT(*) FROM scores) AS TotalScores,
    (SELECT COUNT(*) FROM responses) AS TotalResponses,
    (SELECT COUNT(*) FROM question_bank) AS TotalQuestions,
    (SELECT COUNT(*) FROM student_progress) AS TotalStudentProgress,
    (SELECT COUNT(*) FROM chapter_analytics) AS TotalChapters,
    (SELECT COUNT(*) FROM question_analytics) AS TotalQuestionAnalytics,
    (SELECT COUNT(*) FROM student_risk_report) AS TotalRiskRecords;


