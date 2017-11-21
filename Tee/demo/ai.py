import aiml


alice = aiml.Kernel()

alice.learn('sourse/std-startup.xml')


while True:
    print alice.respond(raw_input('send mes:::'))









