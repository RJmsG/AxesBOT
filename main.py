from mod import *
import mod
import sys

profanity.load_censor_words()
usr=input('username:')
pswd=input('password:')
c = Client(usr, pswd, debug=False)


def on_raw_msg(msg, _):

    print(f"msg: {msg['u']}: {msg['p']}")
    if msg["u"] == "Discord":
        msg['u'] = msg['p'].split(":")[0]
        msg['p'] = msg['p'].split(":")[1].strip()

    args = msg['p'].split(" ")
    if not args[0] == prefix:
        return

    print(f"args: {args}")
    """
    if not msg[u] in ulist:
      ulist.append(msg[u])
      votes.append('0')
    """
    if args[1] == 'run':
      del args[0]
    elif args[1].lower() == 'helpme':
      a = '\nHey, '.join(commands)
      c.send_msg(f"""
Commands: [TIP: {choice(tips)}]
Hey, {a}
      """)
    elif args[1].lower() == "inform":
        c.send_msg("""
Bot information:
  Owned by @AXEstudios
  Bot lib: MeowerBot.py version 1.4.2 (cl3)
  Hosting Platform/src: https://replit.com/@AXEstudios/AxesBOT
  Morph status: ???
""")
    elif args[1] == "world-status":
        req = get("https://api.meower.org/statistics")
        if not req.status_code == 200:
            print(req.text)
            c.send_msg(
                f"Uh oh! I only got shitpost status from: {req.status_code}")
            return
        data = req.json()
        c.send_msg(
            f"users: {data['users']}\nposts: {data['posts']}\nchats: {data['chats']}"
        )
    elif args[1] == "save":
      file = open('memes','w')
      file.writelines('\n'.join(mod.memes))
      file.close()
      file = open('users','w')
      file.writelines('\n'.join(mod.ulist))
      file.close()
      file = open('votes','w')
      file.writelines('\n'.join(mod.votes))
      file.close()
      c.send_msg("Saved session data!")
    elif args[1] == "say":
      del args[0]
      del args[0]
      c.send_msg(' '.join(args))
    elif args[1] == "spam":
      c.send_msg(f'@{msg["u"]} -99999 social credit')
      """
      for i in range(int(args[2])):
        sleep(1)
        c.send_msg('Why should I? Huh?')
      c.send_msg('Why? Why should I?')
      """
    elif args[1] == "meme":
      c.send_msg('meming...')
      a = choice(memes).split("/")
      c.send_msg(f'[{a[len(a) - 1]}: '+'/'.join(a)+']')
    elif args[1] == "newmeme":
      print('newmeme')
      a = args[2].split('/')
      print(a)
      if a[2] in whitelist:
        memes.append(args[2])
        c.send_msg("Added!")
      else:
        c.send_msg("Error: You're image hosting sight was not on the whitelist! This bot is designed to display images on Meower svelte. (it probably wont display on bettermeower though :skull:)")
    elif args[1] == "wait":
      c.send_msg('plase wait. your request will start shortly...')
      sleep(5)
      c.send_msg('Alright, I\'m ready to-')
    elif args[1] == "vote":
      print('Vote user')
      if args[2] in ulist:
        votes[ulist.index(args[2])] = str(int(votes[ulist.index(args[2])]) + 1)
      else:
        ulist.append(args[2])
        votes.append('1')
        print('not in ulist')
      c.send_msg('User now has 1 more vote!')
    elif args[1] == 'votes':
      if msg['u'] in ulist:
        c.send_msg(f"You currently have: {votes[ulist.index(msg['u'])]} votes.")
      else:
        ulist.append(msg['u'])
        votes.append('0')
        c.send_msg(f"Welcome to the vote buiseness, you currently have: {votes[ulist.index(msg['u'])]} votes.")
      print('view votes')
      """
      if len(args) < 3:
        if msg[u] in ulist:
          c.send_msg(f"You currently have: {votes[ulist.index(msg['u'])]} votes.")
        else:
          c.send_msg("Welcome to the Vote buisenes!")
          ulist.append(msg['u'])
          votes.append('0')
          c.send_msg("You dont have any votes yet. Use the vote command to support other people! Be careful, you can't unvote.")
      elif args[3] in ulist:
        c.send_msg(f"User @{args[3]} currently has {votes[ulist.index(args[3])]} votes.")
      else:
        c.send_msg('That user isn\'t in the vote buisness!')
    """
    elif args[1] == 'user':
      c.send_msg('That command doesn\'t exist.. YET...')
    elif args[1] == 'why':
      c.send_msg('"Why" is a common question to ask when your computer stops working. Learn more at')
    elif args[1] == 'tip':
      c.send_msg('Heres a tip: Get a life')
    elif args[1] == 'quit':
      if msg['u'] in admin:
        c.send_msg('Preparing to shut down...')
        file = open('memes','w')
        file.writelines('\n'.join(mod.memes))
        file.close()
        file = open('users','w')
        file.writelines('\n'.join(mod.ulist))
        file.close()
        file = open('votes','w')
        file.writelines('\n'.join(mod.votes))
        file.close()
        sleep(1)
        c.send_msg("Saved session data!")
        sleep(1)
        c.send_msg("Bye mortals.")
        sys.exit(0)
      else:
        c.send_msg(f"@{msg['u']} You dont have permission to do that lmao")
    elif args[1] == 'CLEAR':
      if msg['u'] in admin:
        c.send_msg('CLEARING ALL DATA...')
        mod.memes = []
        mod.ulist = []
        mod.votes = []
        sleep(1)
        c.send_msg('The process isn\'t complete. To fully delete all the data, use the save command.')
      else:
        c.send_msg(f"@{msg['u']} You dont have permission to do that lmao")
    else:
      c.send_msg(f'@{msg[u]} Wdym???')
def on_login():
    if len(sys.argv) >= 2:
        print("--before start msg--")

        owner_inp = input('> >')
        c.send_msg("--owner msg--")
        c.send_msg(f"{owner_inp}")

    msg = f"""Hello mortals.
for help, type: \"{prefix} helpme\""""
    c.send_msg(msg)


def on_error(err):
    print(err)
    c.send_msg("Oh **** I got an error")


c.callback(on_raw_msg)
c.callback(on_login)
c.callback(on_error)

try:
    c.start()
except KeyboardInterrupt:
    run(f"kill -9 {pid()}")
finally:
    run("kill 1")
