create directory my_dir as '/home/fyliu/github/problems/Java/Rdbms/data';

CREATE TABLE emp_load (
    employee_number         CHAR(5), 
    employee_last_name      CHAR(20),
    employee_first_name     CHAR(15),
    employee_middle_name    CHAR(15)
)
ORGANIZATION EXTERNAL (
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY my_dir
    ACCESS PARAMETERS (RECORDS FIXED 62 
        FIELDS (
            employee_number CHAR(2),
            employee_dob CHAR(20),
            employee_last_name CHAR(18),
            employee_first_name CHAR(11),
            employee_middle_name CHAR(11)
        )
    )
    LOCATION ('tmp.csv'));
