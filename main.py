from mod import *
import mod

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
    if args[1].lower() == 'helpme':
      a = '\n'+'\nHey, '.join(commands)
      c.send_msg(f"""
Commands: {a}
      """)
    elif args[1].lower() == "readthedocs":
        c.send_msg("""
Bot information:
  Owned by @AXEstudios
  Bot lib: MeowerBot.py version 1.4.2 (cl3)
  Hosting Platform/src: yo mama
  Morph status: ???
""")
    elif args[1] == "WorldPopulation":
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
      file.writelines(mod.memes)
      file.close()
      
    elif args[1] == "say":
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
      a = random.choice(memes).split(':')
      c.send_msg(f'[{a[0]}: {a[1]}]')
    elif args[1] == "newmeme":
      if args[2][0:23] in whitelist:
        memes.append(f"{args[3]}: {args[2]}")
        c.send_msg("Added!")
      else:
        c.send_msg("Error: You're image hosting sight was not on the whitelist! This bot is designed to display images on Meower svelte.")

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
