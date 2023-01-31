anaconda에서 지원하지 않는 package를 설치해야 하는 경우 pip을 사용해 하는데, 종속성 관리가 어려워 질 수 있다.

이 때 anaconda의 가상환경을 주로 사용하고 싶다면, 아래와 같이 설치한다.

```bash
conda install pip
```

이후 pip를 사용하여 package를 설치하면 된다.

```bash
pip install ~~~
```

이 때 주의해야 할 점은, 가능한한 많은 패키지를 conda 로 먼저 설치하고, 그 이후에 pip으로 설치하는 것이 좋다.

이와 같이 하면 pip install 패키지는 conda list 에서 Channel이 pypi로 되어 있는 것을 확인할 수 있다.

그러면 종속성 관리가 아래와 같이 용이해진다

```bash
conda list --export > packagelist.txt
conda install--file packagelist.txt
```
