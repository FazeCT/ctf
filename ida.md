## IDA TIP & TRICKS 

### IDA REMOTE LINUX DEBUG 

Sample: [ELF C++ - 0 protection](https://www.root-me.org/en/Challenges/Cracking/ELF-C-0-protection)

1. Load the binary into IDA.

2. Locate **/.../IDA/dbgsrv/linux_server64**; paste the file into the same directory as the binary.

![image](https://github.com/FazeCT/ctf/assets/110371121/26ad189a-157a-43a8-ac89-5afb897d2e63)

![image](https://github.com/FazeCT/ctf/assets/110371121/235a5cf0-28c4-4047-8715-acdd640994ea)

3. Open terminal inside the directory, type:

> **ip a**

![image](https://github.com/FazeCT/ctf/assets/110371121/ba27b7c6-165a-4e93-9d31-df7328e896a3)

Copy the inet hostname (**172.22.98.247**).

> **./linux_server64**

![image](https://github.com/FazeCT/ctf/assets/110371121/5e2e9515-3f54-427d-8a25-0a0002de9cc6)

4. In IDA, choose **Remote Linux Debugger**.

![image](https://github.com/FazeCT/ctf/assets/110371121/9ca0e3e6-7bde-46b5-af24-8adb1e8207cb)

5. Go to **Debugger > Process Options...**, set the hostname to the copied hostname from **ip a**.

![image](https://github.com/FazeCT/ctf/assets/110371121/bdf40460-ba87-4f58-87ff-cda710cea9bd)

5a. If you are debugging a binary that requires args (for example, **./binary flag{dummy_flag}**...

-> Put **flag{dummy_flag}** into parameter section.

![image](https://github.com/FazeCT/ctf/assets/110371121/a7a278ae-62f3-4a77-9e02-9ac488adb791)

6. Run the debugger.

6a. Right click on the taskbar, choose **Debugger commands** dor the debugger options to appear.

![image](https://github.com/FazeCT/ctf/assets/110371121/2c6b5af2-7ed6-4d1d-a56a-2f07a6936f47)

7. These buttons...

![image](https://github.com/FazeCT/ctf/assets/110371121/9d3de7be-ff46-422b-9ee1-f1f6e9788bbd)

From left to right:

- Step into: Step into all call instructions (to debug inside functions, ...).

- Step over: Step over all call instructions.

- Step outside: Step over all remaining instructions of a callee and get back to the caller.

8. If your debugger is not stepping inside the pseudo-code (F5) but the assembly code...

-> Turn on **Debugger > Use source-level debugging**.

![image](https://github.com/FazeCT/ctf/assets/110371121/757e3be4-2a01-477a-8b8f-ffab438b89f0)

8a. Press **G** to jump to any address.

![image](https://github.com/FazeCT/ctf/assets/110371121/41249f77-2736-4015-9d37-02eaeee110b1)

8b. Edit register values/flag values at the breakpoint using the panels on the right.

![image](https://github.com/FazeCT/ctf/assets/110371121/aac57cb1-8386-4a4c-893c-dc028a0c74ce)

8c. Press **X** to get an offset's xrefs (where the binary invokes the offset).

![image](https://github.com/FazeCT/ctf/assets/110371121/f18814e6-97e0-4744-bd33-6cc63bf0e319)

8d. Go to **Edit > Segments > Rebase program** and set the value to `0` to get rid of the base addresses.

![image](https://github.com/FazeCT/ctf/assets/110371121/172b5914-0feb-4db8-a2b7-cec3f9e6b4d9)

9. To be updated...
















