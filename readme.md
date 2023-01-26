이 공간은 파이썬 예제 코드를 연습하고 저장하는 공간입니다.

환경: 아나콘다 파이썬 3.8
conda activate python_example

conda list --export > packagelist.txt
conda install --file packagelist.txt
