-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH FROM member_profile
WHERE gender = 'W' AND MONTH(date_of_birth) = 3 AND tlno IS NOT NULL;