import sys, pyperclip


passwords = {'google' : 'googlepass',
            'mac' : 'macpass',
            'facebook' : 'facebookpass'
}

if len(sys.argv) < 2:
    print("HEPP : python pass_manag [account]")
    sys.exit()

account = sys.argv[1]

if account in passwords :
        pyperclip.copy(passwords[account])
        print('Password pour ' + account + ' à été copié avec succes')
else : 
    print("il n'y a pas de mot de passe pour cette demande")