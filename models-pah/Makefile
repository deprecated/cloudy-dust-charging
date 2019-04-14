%.out: %.in
	$D/cloudy.exe < $< > $@


OUTFILES := $(patsubst %.in,%.out,$(wildcard dustrad*.in))
SHELL_OUTFILES := $(patsubst %.in,%.out,$(wildcard shell*.in))

all: $(OUTFILES)

shells: $(SHELL_OUTFILES)
