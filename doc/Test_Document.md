﻿# Test Document
- [Test Document](#test-document)
  - [Black-Box Testing](#black-box-testing)
  - [White-Box Testing](#white-box-testing)
    - [Static White-Box Testing](#static-white-box-testing)
    - [Dynamic White-Box Testing](#dynamic-white-box-testing)
  - [Unit Testing](#unit-testing)
  - [Automatic Testing](#automatic-testing)
## Black-Box Testing
Equivalence class:  
1. M1 = {input sid valid}
2. M2 = {input sid invalid}
3. M3 = {input sid null}
4. D1 = {input sname valid}
5. D2 = {input sname invalid}
6. D3 = {input sname null}
Condition Stub:  

1. C1: input sid in {M1,M2,M3}
2. C2: input sname in {D1,D2,D3}
3. C3: whether take photo in {yes, no}
4. C4: press the add button

Action Stub:  

1. A1: registration success
2. A2: Error exception

Effect Diagram:

![](img/black_test_regist.svg)

Decision table:  
| Rules stub           | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
|----------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| C1:input sid state   | M1  | M1  | M1  | M2  | M2  | M2  | M3  | M3  | M3  | -   |
| C2:input sname state | D1  | D2  | D3  | D1  | D2  | D3  | D1  | D2  | D3  | -   |
| C3:take photo state  | yes | yes | yes | yes | yes | yes | yes | yes | yes | no  |
| C4:press button      | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| A1:Success           | ✔   |     |     |     |     |     |     |     |     |     |
| A2:Error exception   |     | ✔   | ✔   | ✔   | ✔   | ✔   | ✔   | ✔   | ✔   |     |  

Test cases:
| sample number | sample operations                                                      | sample input            | sample output         |
|---------------|------------------------------------------------------------------------|-------------------------|-----------------------|
| 001           | input valid sid <br /> input valid sname<br>   take photo<br>   press button   | 1809853zi0110099<br>   cr   | Registration succeed! |
| 002           | input valid sid<br>   input invalid sname<br>   take photo<br>   press button      | 1809853zi0110098<br>   123  | Error exception!      |
| 003           | input valid sid<br>   input null sname<br>   take photo<br>   press button         | 1809853ji0110097<br>   ""   | Error exception!      |
| 004           | input invalid sid<br>   input valid sname<br>   take photo<br>   press button      | 1809853@iohqwer!<br>   cyx  | Error exception!      |
| 005           | input invalid sid<br>   input invalid sname<br>   take photo<br>   press button    | 1809!@#$%^&*()<br> hpl  | Error exception!      |
| 006           | input invalid sid<br>   input null sname<br>   take photo<br>   press button       | 1809😂😂😂😂 <br>  ""          | Error exception!      |
| 007           | input null sid<br>   input valid sname<br>   take photo<br>   press button         | ""<br>wyy                | Error exception!      |
| 008           | input null sid<br>   input invalid sname<br>   take photo<br>   press button       | ""<br>(^-^)(^-^)(^-^)    | Error exception!      |
| 009           | input null sid<br>   input null sname<br>   take photo<br>   press button          | ""<br>""                 | Error exception!      |
| 010           | input null/(in)valid sid<br>   input null/(in)valid sname<br>   press button   | 1809853zi0110099<br>   cr   | Error exception       |   
> `""""` means null value
## White-Box Testing
### Static White-Box Testing 
Static Testing Tool

In order to fix static logic bugs and identify code styles, including naming regulation, import order and variable definition, we use the tool -- 
[pylint](https://github.com/PyCQA/pylint) for simple the censor among members.  

For example, the testing result about [faceHelper.py](../faceHelper.py) :
```text
************* Module faceHelper
faceHelper.py:40:0: C0325: Unnecessary parens after 'while' keyword (superfluous-parens)
faceHelper.py:1:0: C0103: Module name "faceHelper" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:1:0: C0114: Missing module docstring (missing-module-docstring)
faceHelper.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
faceHelper.py:12:10: E1101: Module 'cv2' has no 'CascadeClassifier' member (no-member)
faceHelper.py:14:11: E1101: Module 'cv2' has no 'cvtColor' member (no-member)
faceHelper.py:14:31: E1101: Module 'cv2' has no 'COLOR_BGR2GRAY' member (no-member)
faceHelper.py:22:14: E1101: Module 'cv2' has no 'CASCADE_SCALE_IMAGE' member (no-member)
faceHelper.py:26:9: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:26:12: C0103: Variable name "y" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:26:15: C0103: Variable name "w" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:26:18: C0103: Variable name "h" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:28:8: E1101: Module 'cv2' has no 'rectangle' member (no-member)
faceHelper.py:33:0: C0103: Function name "faceCapture" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
faceHelper.py:47:12: W0621: Redefining name 'faceCapture' from outer scope (line 33) (redefined-outer-name)
faceHelper.py:34:10: E1101: Module 'cv2' has no 'VideoCapture' member (no-member)
faceHelper.py:44:14: E1101: Module 'cv2' has no 'waitKey' member (no-member)
faceHelper.py:45:11: C0121: Comparison 'ret == True' should be 'ret is True' if checking for the singleton value True, or 'ret' if testing for truthiness (singleton-comparison)
faceHelper.py:47:12: C0103: Variable name "faceCapture" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:48:12: E1101: Module 'cv2' has no 'imshow' member (no-member)
faceHelper.py:50:16: R1723: Unnecessary "elif" after "break" (no-else-break)
faceHelper.py:51:24: C0103: Variable name "x1" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:51:28: C0103: Variable name "y1" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:51:32: C0103: Variable name "x2" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:51:36: C0103: Variable name "y2" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:54:20: E1101: Module 'cv2' has no 'imencode' member (no-member)
faceHelper.py:63:4: E1101: Module 'cv2' has no 'destroyAllWindows' member (no-member)
faceHelper.py:67:0: C0103: Function name "faceRecognize" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
faceHelper.py:67:45: W0622: Redefining built-in 'dir' (redefined-builtin)
faceHelper.py:67:0: R0914: Too many local variables (16/15) (too-many-locals)
faceHelper.py:90:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
faceHelper.py:120:11: W0703: Catching too general exception Exception (broad-except)
faceHelper.py:117:8: C0103: Variable name "minIndex" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:120:4: C0103: Variable name "e" doesn't conform to snake_case naming style (invalid-name)
faceHelper.py:3:0: C0411: standard import "import os" should be placed before "import cv2" (wrong-import-order)
faceHelper.py:4:0: C0411: third party import "import numpy as np" should be placed before "import face_recognition.api as face_recognition" (wrong-import-order)

--------------------------------------------------------------------
Your code has been rated at -0.40/10 (previous run: -0.40/10, +0.00)
```

Walkthrough :

In the walkthrough, it is also important that after the review, the presenter prepare a report on what problems have been found and how to plan to solve the found software defects, referred by [#10](https://github.com/MUST-Quick-Fry/Face-Recognition-Sign-In-System/pull/10#issue-1052853864)


### Dynamic White-Box Testing 
We use **White Box Test** to test 3 different and critical functions in [`UI/utils.py`](../UI/utils.py)
1. `takePhoto` func
    
    Control FLow Graph:
    
    ![](img/take_photo.svg)

    Loop Complexity：

    The loop complexity is 7.  


    Independent Path：

    1. 20 -> 22 -> 25 -> 26 -> 29 -> 30 -> 31 -> 48
    2. 20 -> 22 -> 25 -> 26 -> 29 -> 30 -> 34 -> 35 -> 36-42 -> 43 -> 44-45 -> 48
    3. 20 -> 22 -> 25 -> 26 -> 29 -> 30 -> 34 -> 35 -> 36-42 -> 43 -> 48
    4. 20 -> 22 -> 25 -> 29 -> 30 -> 31 -> 48
    5. 20 -> 22 -> 25 -> 26 -> 29 -> 30 -> 34 -> 35 -> 48
    6. 20 -> 22 -> 25 -> 29 -> 30 -> 34 -> 35 -> 36-42 -> 43 -> 44-45 -> 48
    7. 20 -> 22 -> 25 -> 29 -> 30 -> 34 -> 35 -> 36-42 -> 43 -> 48
    8. 20 -> 22 -> 25 -> 29 -> 30 -> 34 -> 35 -> 48
    9. 20 -> 22 -> 23 -> 48
    10. 20 -> 22 -> 47 -> 48

    Test Cases:

    |              | input                                                                                                                     | expected output |
    |--------------|---------------------------------------------------------------------------------------------------------------------------|-----------------|
    | Test case 1  | userID = 1809853zi0110099<br> os.path.exists(dir) = False<br> opened = False<br>                                                      | Error Exception |
    | Test case 2  | userID = 1809853zi0110099<br> os.path.exists(dir) = False<br> opened = True<br> os.path.exists(img_path)=True<br> unkown_encoding = False<br> | Error Exception |
    | Test case 3  | userID = 1809853zi0110099<br> os.path.exists(dir) = False<br> opened = True<br> os.path.exists(img_path)=True<br> unkown_encoding = True<br>  | Success         |
    | Test case 4  | userID = 1809853zi0110099<br> os.path.exists(dir) = True<br> opened = False<br>                                                       | Error Exception |
    | Test case 5  | userID = 1809853zi0110099<br> os.path.exists(dir) = False<br> opened = True<br> os.path.exists(img_path)=False <br>                       | Error Exception |
    | Test case 6  | userID = 1809853zi0110099<br> os.path.exists(dir) = True<br> opened = True<br> os.path.exists(img_path)=True<br> unknown_encoding = False<br> | Error Exception |
    | Test case 7  | userID = 1809853zi0110099<br> os.path.exists(dir) = True<br> opened = True<br> os.path.exists(img_path)=True<br> unknown_encoding = True<br>  | Success!        |
    | Test case 8  | userID = 1809853zi0110099<br> os.path.exists(dir) = True<br> opened = True<br> os.path.exists(img_path)=False <br>                        | Error Exception |
    | Test case 9  | userID = ""                                                                                                               | Error Exception |
    | Test case 10 | userID = "hahahahaha"                                                                                                     | Error Exception                |

2. `addUser` func

    Control Flow Graph: 
    
    ![](img/add_user.svg)

    Loop Complexity:

    The loop complexity is 5.

    Independent Path:

    1. 50-54 -> 55 -> 56-57 -> 85
    2. 50-54 -> 55 -> 61-62 -> 85
    3. 50-54 -> 55 -> 64-69 -> 70 -> 72 -> 73-78 -> 85
    4. 50-54 -> 55 -> 64-69 -> 70 -> 79 -> 80-81 -> 85
    5. 50-54 -> 55 -> 64-69 -> 82 -> 83-84 -> 85

    Test Cases  
    |             | input                                                                                                                                                               | expected output  |
    |-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
    | Test case 1 | os.path.exists(os.path.join(dir, userImg)) = False                                                                                                                  | Error Exception! |
    | Test case 2 | os.path.exists(os.path.join(dir, userImg)) = True userName = "wyy"<br> userID = ""                                                                                      | Error Exception! |
    | Test case 3 | os.path.exists(os.path.join(dir, userImg)) = True userName = "cr"<br> userID = "1809853zi0110099" len(sql3_helper.query(cmd = testsql)) == 0                            | Success!         |
    | Test case 4 | os.path.exists(os.path.join(dir, userImg)) = True userName = "cr"<br> userID = "1809853zi0110099" len(sql3_helper.query(cmd = testsql)) == 0 database statement = false | Error Exception  |
    | Test case 5 | os.path.exists(os.path.join(dir, userImg)) = True userName = "cr"<br> userID = "1809853zi0110099" len(sql3_helper.query(cmd = testsql)) != 0                            | Error Exception  |

3. `execIdentification` func

    Control Flow Graph:
    
    ![](img/identification.svg)

    Loop Complexity:

    The loop complexity is 6.

    Independent Path:
    1. 102 -> 103 -> 104 -> 140
    2. 102 -> 103 -> 105 -> 106-108 -> 109 -> 110-111 -> 112 -> 113 -> 116 -> 118 -> 119 -> 120-127 -> 128 -> 129-130 -> 140
    3. 102 -> 103 -> 105 -> 106-108 -> 109 -> 110-111 -> 112 -> 113 -> 116 -> 118 -> 119 -> 120-127 -> 128 -> 132-134 -> 140
    4. 102 -> 103 -> 105 -> 106-108 -> 109 -> 110-111 -> 112 -> 113 -> 116 -> 118 -> 119 -> 136-139 -> 140
    5. 102 -> 103 -> 105 -> 106-108 -> 109 -> 110-111 -> 112 -> 115 -> 116 -> 118 -> 119 -> 120-127 -> 128 -> 129-130 -> 140
    6. 102 -> 103 -> 105 -> 106-108 -> 109 -> 110-111 -> 112 -> 115 -> 116 -> 118 -> 119 -> 120-127 -> 128 -> 132-134 -> 140
    7. 102 -> 103 -> 105 -> 106-108 -> 109 -> 110-111 -> 112 -> 115 -> 116 -> 118 -> 119 -> 136-139 -> 140
    8. 102 -> 103 -> 105 -> 106-108 -> 109 -> 118 -> 119 -> 120-127 -> 128 -> 129-130 -> 140
    9. 102 -> 103 -> 105 -> 106-108 -> 109 -> 118 -> 119 -> 120-127 -> 128 -> 132-134 -> 140 
    10. 102 -> 103 -> 105 -> 106-108 -> 109 -> 118 -> 119 -> 136-139 -> 140

    Test Cases
    |              | input                                                                                                                       | expected input   |
    |--------------|-----------------------------------------------------------------------------------------------------------------------------|------------------|
    | Test case 1  | opened = False                                                                                                              | Error Exception! |
    | Test case 2  | opened = True <br> os.path.exists(unknown_path) = True <br> self.count = 0 <br> success = True <br> int(out[0][0]) = 1 <br> | Error Exception! |
    | Test case 3  | opened = True <br> os.path.exists(unknown_path) = True <br> self.count = 0 <br> success = True <br> int(out[0][0]) = 0 <br> | Success!         |
    | Test case 4  | opened = True <br> os.path.exists(unknown_path) = True <br> self.count = 0 <br> success = False <br>                        | Error Exception! |
    | Test case 5  | opened = True <br> os.path.exists(unknown_path) = True <br> self.count = 6 <br> success = True <br> int(out[0][0]) = 0 <br> | Success!         |
    | Test case 6  | opened = True <br> os.path.exists(unknown_path) = True <br> self.count = 6 <br> success = True <br> int(out[0][0]) = 1 <br> | Error Exception! |
    | Test case 7  | opened = True <br> os.path.exists(unknown_path) = True <br> self.count = 6 <br> success = False <br>                        | Error Exception! |
    | Test case 8  | opened = True <br> os.path.exists(unknown_path) = Flase <br> success = True <br> int(out[0][0]) = 1 <br>                    | Error Exception  |
    | Test case 9  | opened = True <br> os.path.exists(unknown_path) = False <br> success = True <br> int(out[0][0]) = 0 <br>                    | Success!         |
    | Test case 10 | opened = True <br> os.path.exists(unknown_path) = False <br> success = False <br>                                           | Error Exception! |

## Unit Testing
We use [unittest](https://docs.python.org/3/library/unittest.html) from **Python Package Index**, the specific codes can referred in [test_unittest.py](../test_unittest.py)  

## Automatic Testing
**Selenium**
We use [**Github Action**](https://docs.github.com/en/actions) to