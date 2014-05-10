ARGS = ""

.PHONY: all

all:
	cd Java/LetTheDataSpeak/ ; \
	ant build -Darguments="$(ARGS)" -verbose ; \
	ant MyMusicApp ;   



