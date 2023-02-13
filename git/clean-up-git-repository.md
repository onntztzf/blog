# 如何清理 Git 仓库

## 仓库原来越大的原因

`git` 会把文件的每一个差异化版本都记录在案。即使你只改动了某个文件的一行内容，`git` 也会生成一个全新的 `blob` 对象来存储新的文件内容。`git gc` 打包或者每次 `git push` 的时候 `git` 都会自动执行一次打包过程，将 `blob` 对象合并成一个包文件，同时会生成一个索引文件，索引文件中包含了每个 `blob` 对象在包文件中的偏移信息，在打包的过程中使用了增量编码方案，只保存 `blob` 对象的不同版本之间的差异，这会减缓仓库变大的速度。但是整体还是一个上涨的过程。

## 处理方法

### 方法一

方法一的核心是清理大文件或者不再需要的文件\(后文统称为冗余文件\)，以及他们所产生的提交记录。**下面的操作一定要三思而行，真的会把文件删除的哟！**

1. 找到所有冗余文件的git记录

   ```text
   git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -5 | awk '{print $1}')"
   ```

   解释一下上面的代码： 1. 倒序列出的提交引用的任何对象的对象id 2. 读取 git 归档后的idx文件，列出所有的对象列表，然后根据列表中的第三项\(size\)进行升序排序，然后取最后 5 项，截取第一列（SHA-1） 3. 取操作一和操作二的交集，便是当前仓库中占用空间最大的5个文件或提交记录

2. 删除冗余文件以及相关提交记录

   删除时，一定要核对好，因为上面一步输出的既包含了提交记录中的大文件，也包含当前仓库中的大文件。

   * 删除文件

     ```text
        git filter-branch --force --index-filter \
        'git rm --cached --ignore-unmatch 文件名' \
        --prune-empty -- --all
     ```

   * 删除文件夹

     ```text
        git filter-branch --force --index-filter \
        'git rm -r --cached --ignore-unmatch 文件夹名' \
        --prune-empty -- --all
     ```

3. 删除缓存对象

   ```text
    git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
    git reflog expire --expire=now --all
    git gc --prune=now
   ```

4. 推送至远程仓库

   当你确认你的操作都没有问题后，就可以强制推送到远程了。

   ```text
    git push --force
   ```

### 方法二

方法二比较暴力，直接**将整个仓库的历史全部删掉**，以达到对git仓库瘦身的目的。

1. 删除所有的远程分支

   ```text
    git branch -r | grep origin | grep -v '>' | grep -v master | xargs -L1 | awk '{sub(/origin\//,"");print}'| xargs git push origin --delete
   ```

2. 删除本地的.git文件夹

   ```text
    rm -rf .git
   ```

3. 初始化本地的git仓库

   ```text
    git init
    git add .
    git commit -m "init"
   ```

4. 将本地的git仓库与已有的远程仓库进行关联

   ```text
   git remote add origin 远程仓库地址(https://xxx.git 或 git@xxx.git 均可)
   ```

5. 强制推送到远程仓库

   ```text
   git push -f origin master
   ```

## 参考资料

1. [git-rev-list](https://git-scm.com/docs/git-rev-list)
2. [git-verify-pack](https://git-scm.com/docs/git-verify-pack)
3. [git-filter-branch](https://git-scm.com/docs/git-filter-branch)
4. [为什么你的 Git 仓库变得如此臃肿](https://www.jianshu.com/p/7231b509c279)
5. [为什么.git/objects/pack文件夹变得非常大，处理git仓库臃肿](https://www.jianshu.com/p/4f2ccb48da77)

> Title: 如何清理 git 仓库
>
> Date: 2020.07.28
>
> Author: zhangpeng
>
> Github: [https://github.com/gh-zhangpeng](https://github.com/gh-zhangpeng)

