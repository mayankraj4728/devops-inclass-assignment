# Linux Homework Tasks

## Task 1: Soft Link & Hard Link

### Difference Between Soft Link and Hard Link

| Soft Link (Symbolic Link) | Hard Link |
|---------------------------|-----------|
| Points to the original file path | Points directly to the file inode |
| Can link across file systems | Cannot link across file systems |
| Can link directories | Cannot link directories (normally) |
| Breaks if original file is deleted | Still works if original file is deleted |
| Created using `ln -s` | Created using `ln` |

### Commands

#### Create a File

```bash
touch file1.txt
```

#### Create a Soft Link

```bash
ln -s file1.txt softlink.txt
```

#### Create a Hard Link

```bash
ln file1.txt hardlink.txt
```

#### View Links

```bash
ls -li
```

#### Delete Soft Link

```bash
rm softlink.txt
```

#### Delete Hard Link

```bash
rm hardlink.txt
```

#### Delete Original File

```bash
rm file1.txt
```



**Q: What is the difference between a soft link and a hard link?**

**Answer:**  
A soft link stores the path of the original file and breaks if the original file is deleted. A hard link points directly to the file inode, so it continues to work even if the original file is deleted.

---

## Task 2: adduser vs useradd

### Difference

| adduser | useradd |
|----------|----------|
| User-friendly command | Low-level command |
| Creates home directory automatically | Requires additional options |
| Prompts for password and user details | Does not prompt |
| Preferred on Ubuntu | Mainly used for scripting |

### Recommended Command

Ubuntu recommends:

```bash
sudo adduser testuser
```

### Example

Create a user:

```bash
sudo adduser testuser
```

Switch to the user:

```bash
su - testuser
```

Delete the user:

```bash
sudo deluser testuser
```

---

## Task 3: journalctl

### What is journalctl?

`journalctl` is used to view and manage logs collected by systemd's journal service.

### Useful Commands

View all logs:

```bash
journalctl
```

View recent logs:

```bash
journalctl -n 50
```

Follow logs in real time:

```bash
journalctl -f
```

View logs from current boot:

```bash
journalctl -b
```

View logs for a specific service:

```bash
journalctl -u ssh
```

Example for Docker:

```bash
journalctl -u docker
```

View logs since today:

```bash
journalctl --since today
```

View logs for the last hour:

```bash
journalctl --since "1 hour ago"
```

---

## Task 4: Linux Command Cheat Sheet

### File & Directory Commands

```bash
pwd
ls
ls -l
ls -a
cd
mkdir
rmdir
rm
cp
mv
touch
cat
```

### File Viewing Commands

```bash
less
more
head
tail
tail -f
```

### Search Commands

```bash
find
grep
which
```

### User Management Commands

```bash
whoami
who
id
adduser
useradd
passwd
```

### Process Commands

```bash
ps
top
htop
kill
killall
```

### Disk Commands

```bash
df -h
du -sh
```

### Permission Commands

```bash
chmod
chown
chgrp
```

### Networking Commands

```bash
ping
ip a
ss
curl
wget
```

### System Information Commands

```bash
uname -a
hostname
uptime
free -h
```

---