# EasyDiscordPy

### 1 Step:
- Download file `main.py`, put that file in directory with your **discord bot** file.

### 2 Step:
- In your **discord bot** file import module with command:
```python
import main
```
### 3 Step:
- You need to install module `art`:
```python
pip install art
```
### 4 Step:
- Then we go to code in your **discord bot** file, assign class variable:
```python
cmd = main.Main()
```
- We have some methods;
1. AddRole to user:
```python
await cmd.AddRole(ctx, bot, role, user)
```
2. RemoveRole from user:
```python
await cmd.DelRole(ctx, bot, role, user)
```
3. Random integer:
```python
cmd.Random(min, max)
```
4. TextToArt:
```python
await cmd.TextToArt(ctx, bot, text)
```
5. Spamming!
```python
await cmd.Spam(ctx, text, count)
```
