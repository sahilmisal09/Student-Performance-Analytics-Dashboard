USE StudentPerformanceAnalytics;

--- 01. Total Students
SELECT COUNT(*) AS TotalStudents
FROM students;

--- 02. Total Tests Conducted
SELECT COUNT(*) AS TotalTests
FROM tests;

--- 03. Average School Percentage
SELECT ROUND(AVG(percentage),2) AS AveragePercentage
FROM scores;

--- 04. Overall Pass Percentage
SELECT ROUND(COUNT(CASE WHEN pass_fail='Pass' THEN 1 END)*100.0/COUNT(*), 2) AS PassPercentage
FROM scores;

--- 05. Number of High-Risk Students
SELECT COUNT(*) AS HighRiskStudents
FROM student_risk_report
WHERE risk_level='High Risk';

--- 06. Top 10 Students
SELECT TOP 10
student_id,
avg_percentage
FROM student_progress
ORDER BY avg_percentage DESC;

--- 07. Bottom 10 Students
SELECT TOP 10
student_id,
avg_percentage
FROM student_progress
ORDER BY avg_percentage ASC;

--- 08. Students Who Failed
SELECT
student_id,
test_id,
percentage
FROM scores
WHERE pass_fail='Fail';

--- 09. Students Scoring Above 90%
SELECT
student_id,
test_id,
percentage
FROM scores
WHERE percentage>=90;

--- 10. Grade Distribution
SELECT
grade,
COUNT(*) AS Total_Number
FROM scores
GROUP BY grade
ORDER BY grade;

--- Subject Analysis
--- 11. Subject-wise Average
SELECT
subject,
ROUND(AVG(percentage),2) AveragePercentage
FROM scores
GROUP BY subject
ORDER BY AveragePercentage DESC;

--- 12. Pass Percentage by Subject
SELECT
subject,
ROUND(COUNT(CASE WHEN pass_fail='Pass' THEN 1 END)*100.0/COUNT(*),2) AS PassPercentage
FROM scores
GROUP BY subject;

--- 13. Most Difficult Subject
SELECT TOP 1
subject,
AVG(percentage) AverageScore
FROM scores
GROUP BY subject
ORDER BY AverageScore;

--- 14. Best Performing Subject
SELECT TOP 1
subject,
AVG(percentage) AverageScore
FROM scores
GROUP BY subject
ORDER BY AverageScore DESC;

--- Test Analysis
--- 15. Test Type Performance
SELECT
test_type,
ROUND(AVG(percentage),2) AverageScore
FROM scores
GROUP BY test_type;

--- 16. Performance by Difficulty
SELECT
test_difficulty,
ROUND(AVG(percentage),2) AverageScore
FROM scores
GROUP BY test_difficulty;

--- 17. Performance by Term
SELECT
term,
ROUND(AVG(percentage),2) AverageScore
FROM scores
GROUP BY term;

--- Chapter Analytics
--- 18. Weakest Chapters
SELECT TOP 10
chapter,
accuracy_rate
FROM chapter_analytics
ORDER BY accuracy_rate;

--- 19. Strongest Chapters
SELECT TOP 10
chapter,
accuracy_rate
FROM chapter_analytics
ORDER BY accuracy_rate DESC;

--- 20. Subject-wise Chapter Accuracy
SELECT
subject,
ROUND(AVG(accuracy_rate),2) AverageAccuracy
FROM chapter_analytics
GROUP BY subject;

--- Question Analytics
--- 21. Most Difficult Questions
SELECT TOP 10
question_id,
accuracy_rate
FROM question_analytics
ORDER BY accuracy_rate;

--- 22. Easiest Questions
SELECT TOP 10
question_id,
accuracy_rate
FROM question_analytics
ORDER BY accuracy_rate DESC;

--- 23. Question Difficulty Distribution
SELECT
difficulty,
COUNT(*) TotalQuestions
FROM question_bank
GROUP BY difficulty;

--- Risk Analysis
--- 24. Students by Risk Level
SELECT
risk_level,
COUNT(*) Students
FROM student_risk_report
GROUP BY risk_level;

--- 25. High-Risk Students Requiring Intervention
SELECT
student_id,
avg_percentage,
attendance_category,
intervention_required
FROM student_risk_report
WHERE risk_level='High Risk'
ORDER BY avg_percentage DESC;

--- Student Performance with Subject
SELECT
s.student_id,
t.subject,
sc.percentage
FROM scores sc
JOIN students s
    ON sc.student_id = s.student_id
JOIN tests t
    ON sc.test_id = t.test_id;


--- Student Performance by Subject
SELECT
s.student_id,
t.subject,
AVG(sc.percentage) AveragePercentage
FROM scores sc
JOIN students s
    ON sc.student_id = s.student_id
JOIN tests t
    ON sc.test_id = t.test_id
GROUP BY
s.student_id,
t.subject
ORDER BY
s.student_id;

