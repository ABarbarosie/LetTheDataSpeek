ARGS = ""

.PHONY: all

all:
	cd Java/LetTheDataSpeak/ ; \
	ant build -verbose ; \
	ant MyMusicApp -Darguments="$(ARGS)";   



