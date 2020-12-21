- Install app on device with `adb install zero.apk` on emulator or device
- App has an input and a button, but does not seem to do anything.
- App show hint: 'Where else can output go? [PICO]'
- Show device output with `adb logcat` shows the flag on button-press:
```shell
12-18 14:58:01.851  2015  2015 I PICO    : picoCTF{a.moose.once.bit.my.sister}
```

