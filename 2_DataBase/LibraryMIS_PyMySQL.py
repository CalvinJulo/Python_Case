# !/usr/bin/env python
# -*-coding:utf-8 -*-

# 在本地创建一个图书数据表


import pymysql
class DB:
    def __init__(self):
        self.con = pymysql.connect(
            user="root",
            password="@@@@@@",
            host="localhost",
            database="mysql"
        )

        self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)
        sql_create = "create table if not exists %s (%s)" % ('books', 'id Int, name varchar(255), position Int,status varchar(255), borrorwer varchar(255)')
        self.cur.execute(sql_create)

    def query_sql(self, sql):
        """
        查询sql方法
        :param sql: sql语句
        :return: 返回查询的结果
        """

        self.cur.execute(sql)
        return self.cur.fetchall()

    def updata_sql(self, sql):
        """
        修改sql
        :param sql:
        :return:
        """

        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        """
        关闭游标，断开链接
        :return:
        """
        self.cur.close()
        self.con.close()


class Library(object):

    def __init__(self):
        self.DB = DB()

    def add_book(self):
        """
        添加图书
        :return:
        """
        print("*************添加图书*************")
        name = input("请输入书名：")
        position = input("请输入图书存放的位置：")
        if name and position:
            sql = f'insert into books(name,position) value("{name}","{position}")'
            self.DB.updata_sql(sql)
            print("添加成功！")

            n = input("继续添加请输入1: 回车返回主菜单:")
            # 判断用户输入的是否为 1, 为 1 则调用自身，再次添加图书
            if n == "1":
                self.add_book()
        else:
            print("添加失败，书名或位置不能为空！")

    def update_book(self):
        """
        修改图书
        :return:
        """
        print("*************修改图书*************")
        book_id = input("请输入图书id:")
        # 判断查询的书籍 id 是否存在
        res = self.DB.query_sql(f"select * from books where id = {int(book_id)}")
        if res:
            print("当前图书的信息:", res)
            # 判断如果用户不输入图书名称，则使用之前的图书名称
            name = input("请输入书名，不修改输入回车:") or res[0]['name']
            position = input("请输入图书存放的位置, 不修改输入回车: ") or res[0]['position']
            sql = f'update books set name="{name}",position="{position}" where id={id}'
            self.DB.updata_sql(sql)
            print("修改成功！")
            n = input("继续修改请输入1, 回车返回主菜单：")
            if n == "1":
                self.update_book()

        else:
            print("您输入的书籍id不存在")

    def del_book(self):
        """
        删除图书
        :return:
        """
        print("***********删除图书***************")
        book_id = input("请输入删除图书的id:")
        # 判断删除的书籍 id 是否存在
        res = self.DB.query_sql(f"select * from books where id = {book_id}")
        if res:
            print("您要删除的信息如下：", res)
            is_delect = input("确认删除请输入1, 不删除请回车")
            if is_delect == "1":
                sql = f'delete from books where id={id}'
                self.DB.updata_sql(sql)
                print("删除成功！")

                # 判断是否要继续删除
                n = input("继续删除请输入1, 否则按回车：")
                if n == "1":
                    self.del_book()
        else:
            print("您输入的id对应的书籍不存在！")

    def query_book(self):
        """
        查询图书
        :return:
        """
        print("**************查询图书*****************")
        name = input("请输入您要查询的书籍名称:")

        sql = f'select * from books where name = "{name}"'
        res = self.DB.query_sql(sql)
        if res:
            for i in res:
                print(i)
            n = input("继续查询请输入1，否则回车")
            if n == "1":
                self.query_book()
        else:
            print("图书馆中暂无该书籍！")

    def book_list(self):
        """图书列表"""
        sql = "select * from books;"
        res = self.DB.query_sql(sql)
        for i in res:
            print(f"编号：{i['id']}, 书名：{i['name']}, 位置：{i['position']}, 状态:{i['status']}, 借阅人：{i['borrorwer']}")

    def revert_book(self):
        """归还图书"""
        book_id = input("请输入图书编号:")
        res = self.DB.query_sql(f"select * from books where id = {book_id}")
        if res:

            if res[0]['status'] != 2:
                print("该书籍当前为待出借状态，无需归还！")
            else:
                sql = f'update books set borrorwer = NULL, status=1 where id={book_id}'
                self.DB.updata_sql(sql)
                print("归还成功！")
                n = input("如需规划请输入1，否则按回车")
                if n == "1":
                    self.revert_book()

        else:
            print("规划的图书编号不存在！")

    def lend_book(self):
        """借阅图书"""
        print("**********借阅图书************")
        book_id = input("请输入借阅图书的编号id:")
        res = self.DB.query_sql(f"select * from books where id = {book_id}")
        # 判断借阅的书籍 id 是否存在
        if res:
            # 判断图书状态，如果状态为 2 被借阅，则无法出借
            if res[0]['status'] == 2:
                print("该书籍已被他人借阅！")
            else:
                print("您借阅的图书内容为:", res)
                name = input("请输入您的名称:")
                res = f"select * from books where borrorwer = '{name}'"
                lend_list = self.DB.query_sql(res)
                # 判断每人最多只能借阅5本书
                if len(lend_list) >= 5:
                    print("每人最多只能借阅5本书！")
                else:
                    sql = f'update books set borrorwer = "{name}",status=2 where id={id}'
                    self.DB.updata_sql(sql)
                    print("借阅成功！")
                    n = input("继续借阅请输入1，否则回车:")
                    if n == "1":
                        self.lend_book()
        else:
            print("您借阅的书籍不存在！")

    def quit(self):
        self.DB.close()
        print("程序已退出，欢迎下次使用~")

    def bookmenu(self):
        """打印菜单"""
        print('-----------菜单------------')
        print("【1】:添加图书")
        print("【2】:修改图书")
        print("【3】:删除图书")
        print("【4】:查询图书")
        print("【5】:图书列表")
        print("【6】:出借图书")
        print("【7】:归还图书")
        print("【8】:退出")

    def main(self):
        print("************欢迎进入图书管理*****************")
        while True:
            self.bookmenu()
            number = input("请输入你的选项:")
            if number == '1':
                self.add_book()
            elif number == '2':
                self.update_book()
            elif number == '3':
                self.del_book()
            elif number == '4':
                self.query_book()
            elif number == '5':
                self.book_list()
            elif number == '6':
                self.lend_book()
            elif number == '7':
                self.revert_book()
            elif number == '8':
                self.quit()
                break
            else:
                print("您输入的选项有误！")


if __name__ == '__main__':
    books = Library()
    books.main()
