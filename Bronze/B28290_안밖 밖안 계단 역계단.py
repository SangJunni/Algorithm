info = {'fdsajkl;':'in-out','jkl;fdsa':'in-out','asdf;lkj':'out-in',';lkjasdf':'out-in','asdfjkl;':'stairs',';lkjfdsa':'reverse'}
line = input()
if line in info:
    print(info[line])
else:
    print('molu')