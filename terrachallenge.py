from cryptography.fernet import Fernet

key = b'QBShfFGhSYZ9uC_G35ZdNLzNR0m_FDrTXxuo-fDljg0='

f = Fernet(key)

token = f.encrypt(b'gAAAAABdLZ4U_F4a89F7rtlylp62cjZ73AjWWYbxfjkrfF2ONXKdrqPW_Fs9tP9jtp2p3WjBGo9ILuXr6O0lqUm3WXQL8I3Z5nMVACEQ9aPah1USfGrspw2r6PtmI0zcK3i5u0eTtW')

retrieve = f.decrypt(token)

print (retrieve.decode('utf-8'))
