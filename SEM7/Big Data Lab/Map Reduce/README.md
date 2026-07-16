# Running MapReduce in WSL (Windows Subsystem for Linux)

This guide explains how to set up and run the Python MapReduce job (Line, Word, and Character Count) inside WSL using Apache Hadoop.

---

## 1. Prerequisites (Setup Java & Hadoop in WSL)

Open your WSL terminal and run the following commands to install Java and set up Hadoop:

### Step A: Install Java 8
Hadoop requires Java. Install OpenJDK 8:
```bash
sudo apt update
sudo apt install openjdk-8-jdk -y
```

### Step B: Download and Extract Hadoop
Download Apache Hadoop 3.3.6 and extract it into `/usr/local/hadoop`:
```bash
cd ~
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop
```

### Step C: Configure Environment Variables
Open your `~/.bashrc` file:
```bash
nano ~/.bashrc
```
Scroll to the bottom of the file and paste:
```bash
# Java Configuration
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Hadoop Configuration
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```
Save and exit (`Ctrl + O`, `Enter`, then `Ctrl + X`). Reload the terminal configurations:
```bash
source ~/.bashrc
```
Verify the installation works:
```bash
hadoop version
```

---

## 2. Running the MapReduce Job in WSL

1. Navigate to this directory in your WSL terminal:
   ```bash
   cd "/mnt/a/COLLEGE WORKS/College-work/SEM7/Big Data Lab/Map Reduce"
   ```
   *(Note: WSL automatically mounts your Windows drives under `/mnt/`)*

2. Make sure the scripts are executable:
   ```bash
   chmod +x mapper.py reducer.py
   ```

3. Run the MapReduce job using Hadoop Streaming:
   ```bash
   hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
     -input input.txt \
     -output output_wsl \
     -mapper "python3 mapper.py" \
     -reducer "python3 reducer.py"
   ```

4. View the job results:
   ```bash
   cat output_wsl/part-00000
   ```

---

## 3. Quick Local Testing (Without Hadoop)
If you want to test your python scripts instantly using Unix/Linux pipes:
```bash
cat input.txt | python3 mapper.py | sort | python3 reducer.py
```
