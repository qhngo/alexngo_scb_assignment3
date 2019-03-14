1. For the original source code nbody.py, since the target is to monitor the execution time,
   I put few extra lines to compute total execution time in seconds (nbody_mod.py)

2. The overall expectations are as follows.
    - Make the source code more readable by reducing complicated function call
    - Shorten execution time. The objective is to finish within 30 seconds

3. For a start, first, I create 4 copies of nbody_mod.py, which are
   nbody_1.py, nbody_2.py, nbody_3.py, and nbody_4.py, respectively.
   Then, I will follow suggestions given in the assignment's webpage, which are:
    - No.1 Reducing function call overhead (reflected in nbody_1.py)
    - No.2 Using alternatives to membership testing of lists (nbody_2.py)
    - No.3 Using local rather than global variables (nbody_3.py)
    - No.4 Using data aggregation to reduce loop overheads (nbody_4.py)
   
   For each change made in the file, there will be some comment to explain the purpose or the difference.
   Then, I monitor execution time of each modified file. The result is recorded in Benchmark.xlsx

4. It is noted that **items No.1 and No.4 made a significant impact on the performance**.

5. All changes will be combined and reflected in nbody_opt.py. Execution time of nbody_opt.py is also recorded.
   **Relative Speedup achieved = 94/26.2 = 3.58 times**

6. To execute the source code, one can run each mentioned file on PyCharm Community Edition,
   or run on command-line interface using "python [filename].py"
   (python.exe should be registered in system path though).

   Output will look like this (last few lines):
    -0.1690074067381597
    -0.1690293205067914
    -0.1690918027627932
    -0.16908292959391336
    -0.16903991544245178
    -0.1690052254059413
    -0.16903656773671472
    -0.1690941031888828
    -0.16907846621158512
    -0.16903274720857253
    -0.16900284987914624
    -0.1690462807512239
    -0.16909717678662617
    -0.16907293588676073
    -0.1690262858527701
    1. Execution time (s) = xx.xxxxx

7. It is necessary to mention that if suggestions are followed closely and correctly,
   we are surely able to reach the objective.
   However, to further enhance the performance, one can think of using other approaches/languages,
   such as Cython (Python with C data types) which is notably faster then pure Python with some
   potential trade offs for maintainability and compatibility.