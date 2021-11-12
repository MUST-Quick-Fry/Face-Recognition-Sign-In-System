Equivalence class:  
1. M1 = {input sid valid}
2. M2 = {input sid invalid}
3. M3 = {input sid null}
4. D1 = {input sname valid}
5. D2 = {input sname invalid}
6. D3 = {input sname null}
Condition stub:  

1. C1: input sid in {M1,M2,M3}
2. C2: input sname in {D1,D2,D3}
3. C3: whether take photo in {yes, no}
4. C4: press the add button

Action stub:  

1. A1: registration success
2. A2: Error exception

Decision table:  
| Rules stub           | 1   | 2   | 3   | 4   |
|----------------------|-----|-----|-----|-----|
| C1:input sid state   | M1  | M1  | M1  | -   |
| C2:input sname state | D1  | D2  | D3  | -   |
| C3:take photo state  | yes | yes | yes | no  |
| C4:press button      | yes | yes | yes | yes |
| A1:Success           | ✔   |     |     |     |
| A2:Error exception   |     | ✔   | ✔   | ✔   |
