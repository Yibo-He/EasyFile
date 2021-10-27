class User:

    @classmethod
    def from_db(cls, username, db):
        '''
            Instantiate the user from database using username

            Parameters:
                username(str): username
                db - the type is the same as the return value of pymysql.connect 
 
            Returns:
                a instance of class User
                
        '''
        #TODO



    def __init__(self, username):
        self.username = username
        self.password = password # password pre
        self.role = role # 角色，0表示管理员，1表示普通用户
    
    def get_allinfo(self):
        '''
            return info of user        
        '''
        print('username: {}, password: {}, role: {}'.format(self.username, self.password, self.role))
    
    def in_db(self, db):
        '''
            Parameters:
                db - the type is the same as the return value of pymysql.connect 
 
            Returns:
                True or False
        '''

    
    

