%.out: %.in
	$D/cloudy.exe < $< > $@


OUTFILES := $(patsubst %.in,%.out,$(wildcard dustrad*.in))

all: $(OUTFILES)
