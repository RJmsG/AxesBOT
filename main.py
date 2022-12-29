from mod import *

profanity.load_censor_words()

c = Client(env["username"], env["password"], debug=False)


def on_raw_msg(msg, _):

    print(f"msg: {msg['u']}: {msg['p']}")
    if msg["u"] == "Discord":
        msg['u'] = msg['p'].split(":")[0]
        msg['p'] = msg['p'].split(":")[1].strip()

    args = msg['p'].split(" ")
    if not args[0] == prefix:
        return

    print(f"args: {args}")
    if args[1].lower() == 'help':
        c.send_msg("""
commands:
  '~! help'
  '~! comic'
  '~! botinfo'
  '~! quote'
  '~! webhook <msg>' (only works if @webhooks is online)
  '~! HttpCat'
  '~! HttpDog'
	'~! HttpMeower'
  '~! CatFact'
  '~! AnimalPic'
  '~! Meower_Stats'
      """)

    elif args[1].lower() == "comic":
        resp = get("https://random-xkcd-img.herokuapp.com/")
        data = resp.json()
        if not profanity.contains_profanity(data["title"]):
            c.send_msg(f"{data['title']}\n\n[img:{data['url']}]")
        else:
            c.send_msg(
                "im sorry but the comic that the Api chose was blocked by better profainty"
            )
            c.send_msg("~! commic")
    elif args[1].lower() == "botinfo":
        c.send_msg("""
Bot information:
  Owned by @ShowierData9978
  Bot lib: MeowerBot.py version 1.4.2 (cl3)
  Hosting Platform/src: https://replit.com/@showierdata9971/ComicBot
""")
    elif args[1] == "quote":
        try:
            req = get(
                "https://api.quotable.io/random?maxLength=100",
                timeout=5,
                headers={
                    "User-Agent":
                    "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
                })
            req.raw.chunked = True  # Fix issue 1
            req.encoding = 'utf-8'  # Fix issue 2
            if not req.status_code == 200:
                c.send_msg(
                    f"I couldn't get a quote from quotable.io, status: {req.status_code}"
                )
                return

            data = json.loads(req.text)
            if profanity.contains_profanity(data["content"]):
                c.send_msg(
                    "im sorry but the quote that the Api chose was blocked by better profainty"
                )
                c.send("~! quote")
                return
            c.send_msg(f"{data['content']} - {data['author']}")
        except Exception as e:
            c.send_msg(
                f"I couldn't get a quote from quotable.io, with error:\n {e.__class__.__name__}: {e}"
            )
    elif args[1] == "webhook":
        req = post("https://webhooks.meower.org/post/home",
                   json={
                       "username": msg['u'],
                       "post": " ".join(args[2:])
                   })
        if not req.status_code == 200:
            print(f"{req.text}")
            c.send_msg(f"I couldn't post to webhooks: {req.status_code}")
            return
    elif args[1] == "HttpCat":
        code = choice(http_status)

        c.send_msg(
            f"code: {code['status']}\nmessage: {code['message']}\n[{code['status']}:https://http.cat/{code['status']}.jpg"
        )
        return
    elif args[1] == "HttpDog":
        code = choice(http_status)

        c.send_msg(
            f"code: {code['status']}\nmessage: {code['message']}\n[{code['status']}:https://http.dog/{code['status']}.jpg"
        )
        return
    elif args[1] == "CatFact":
        req = get("https://meowfacts.herokuapp.com/")
        if not req.status_code == 200:
            print(req.text)
            c.send_msg(
                f"I could not get a cat fact from  https://meowfacts.herokuapp.com/: {req.status_code}"
            )
            return
        c.send_msg(req.json()['data'][0])
    elif args[1] == "HttpMeower":
        code = choice(http_status)
        c.send_msg(
            f"{code['status']}\nmessage: {code['message']}\n[{code['status']}:https://http.meower.org/{code['status']}.jpg]"
        )
    elif args[1] == "AnimalPic":
        animal = choice(["shibes", "cats", "birds"])
        req = get(f"http://shibe.online/api/{animal}")
        if not req.status_code == 200:
            print(req.text)
            c.send_msg(
                f"I could not get a cat fact from  https://meowfacts.herokuapp.com/: {req.status_code}"
            )
            return
        c.send_msg(req.json()[0])
    elif args[1] == "Meower_Stats":
        req = get("https://api.meower.org/statistics")
        if not req.status_code == 200:
            print(req.text)
            c.send_msg(
                f"I somehow could not get the meower API: {req.status_code}")
            return
        data = req.json()
        c.send_msg(
            f"users: {data['users']}\nposts: {data['posts']}\nchats: {data['chats']}"
        )


def on_login():
    if len(sys.argv) >= 2:
        print("--before start msg--")

        owner_inp = input('> >')
        c.send_msg("--owner msg--")
        c.send_msg(f"{owner_inp}")

    msg = """
Formaly named Comics

Do '~! Help'

  """
    c.send_msg(msg)


def on_error(err):
    print(err)
    c.send_msg("I'm sorry, but something went wrong")


c.callback(on_raw_msg)
c.callback(on_login)
c.callback(on_error)

try:
    c.start()
except KeyboardInterrupt:
    run(f"kill -9 {pid()}")
finally:
    run("kill 1")
