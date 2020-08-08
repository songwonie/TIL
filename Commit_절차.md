## GitHub Commit 절차
 
- 참고링크:

		https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html
	
		https://backlog.com/git-tutorial/kr/stepup/stepup2_6.html	
___

- 단계
	1. '문서/GitHub 폴더/해당 레포지토리 폴더' 위치에서 GitBash Here !



	2. $ git init				로컬의 해당 폴더에 Git 초기화!



	3. $ git add .				로컬의 작업한 파일들을 스테이지에 올림!


	   $ git add 폴더명(파일명) 		해당 폴더/파일 스테이지에 올림!


	
	4. $ git status				스테이지에 올린 작업한 파일명을 확인!


	
	5. $ git commit -m "메세지내용"		컴밋 메세지 적기! (각 브랜치별로 적용하는게 좋음)



	6. $ git remote add origin https://github.com/songwonie/FaceRecognition_proj.git

						해당 레포지토리 주소로 원격저장소 연결!



	
	7. $ git checkout -b dev(브랜치 생성시)  or  git checkout dev

	   					dev 브랜치를 생성하거나 이동!




	8. $ git checkout -b feature/detailModule dev	dev 브랜치에서 feaure 브랜치를 분기!



	

	9. $ git push origin feature/detailModule	feature 브랜치에 원격저장소에 올리기!
							
	   (이상태면, github 상에서는 feature 브랜치에 commit 되어 있고, github 상의 브랜치는
	    dev 브랜치는 보이지 않음!)



	10. $ git checkout dev  ->   git merge --no-ff feature/detailModule

							dev 브랜치로 이동하고, dev 브랜치에 feature 브랜치를 병합!




	11. $ git commit -m "메세지내용"		dev 브랜치에 올릴 commit 메세지 적기!




	12. $ git push origin dev			github에 dev 브랜치를 push 하기!




	13. $ git checkout master			master로 이동!




	14. $ git merge --no-ff	dev			dev브랜치를 master 브랜치 병합 	




	15. $ git commit -m "메세지내용"		master에 올릴 commit 메세지 적기!




	16. $ git push origin master			master 버전 완성!




	17. $ git push origin +master			강제로 push하기!	




	### release(배포) 브랜치와 hotfix(버그수정) 브랜치!!!

	  위 절차들을 통해서 feature -> dev -> master로 이어지는 단계를 확인!

	  배포 브랜치를 만드는 이유?!	팀원들과 정해진 배포 일정을 구성하고 프로젝트 수행을 위해!

	  	 			배포 브랜치는 최종적인 버그 수정, 문서 추가 역활!

	  				그래서 기본적으로 모든 기능이 정상적으로 동작하는 상태여야 한다!

		
	  1. $ git checkout -b release-1.2 dev		dev 브랜치에서 release 브랜치 분기!



	  2. $ git checkout master -> git merge --no-ff release-1.2	

							master 브랜치 상에서 release 브랜치 병합!


	  3. $ git tag -a 1.2				merge한 커밋에 release 버전 태그를 부여!



	  4. $ git checkout dev				dev 브랜치에도 release 브랜치의 변경사항을 그대로 적용!


	  5. $ git merge --no-ff release-1.2		dev 브랜치에 release 브랜치 병합!


	  6. $ git branch -d release-1.2		release-1.2 브랜치 삭제

							feature 브랜치도 dev 브랜치에 병합하게 되면

							지워준다! 


		배포한 버전에 긴급하게 수정을 해야할 경우 hotfix 브랜치를 만든다!


		1. $ git checkout -b hotfix-1.2.1 master	master에서 바로 분기한다!


		2. $ git checkout master -> git merge --no-ff hotfix-1.2.1

							필요한 부분을 수정한 후, master 상에서

							긴급수정한 부분을 merge 한다!



		3. $ git tag -a 1.2.1			병합한 커밋에 버전 이름을 태그로 부여


		4. $ git checkout dev  ->  git merge --no-ff hotfix-1.2.1 	dev 브랜치에도 수정사항을 반영!





	- GitHub에서 Feature 브랜치로 협업하는 workflow!


	    참고링크 : https://gmlwjd9405.github.io/2017/10/27/how-to-collaborate-on-GitHub-1.html



	- 오픈소스 프로젝트의 참여자가 자신의 local 공간과 원격저장소 각각, git 저장소를 가지는 방식!


	    참고링크 : https://gmlwjd9405.github.io/2017/10/28/how-to-collaborate-on-GitHub-2.html



	- 협업 프로젝트시에 fork/clone/branch/PR(pull-request) 등 필요 과정!

	    참고링크 : https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/  		
						
