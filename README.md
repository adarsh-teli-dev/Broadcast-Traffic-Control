# 🚀 Broadcast Traffic Control using SDN (POX + Mininet)

---

## 🧩 1. Problem Statement

In conventional networks, broadcast packets are blindly flooded across all devices within a network segment. While simple, this behavior leads to:

* Unnecessary bandwidth consumption
* Increased latency
* Potential broadcast storms

This project proposes an **SDN-based solution** to intelligently control broadcast traffic using a centralized controller.

---

## 🏗️ 2. SDN Architecture

The system follows a standard **Software Defined Networking (SDN)** model:

| Layer             | Component               | Role                        |
| ----------------- | ----------------------- | --------------------------- |
| Application Plane | Broadcast Control Logic | Defines traffic rules       |
| Control Plane     | POX Controller          | Decides forwarding behavior |
| Data Plane        | Open vSwitch (Mininet)  | Executes flow rules         |

### 🔁 Working Principle

1. Switch receives packet
2. Unknown packets → sent to controller (`PacketIn`)
3. Controller decides:

   * Allow forwarding
   * Drop broadcast
4. Flow rules applied dynamically

---

## 🌐 3. Mininet Topology Design

A **linear topology** is used:

```
h1 ---- s1 ---- s2 ---- h2
```

### Components:

* **Hosts:** h1, h2
* **Switches:** s1, s2
* **Controller:** Remote POX Controller

### Why this topology?

* Demonstrates broadcast propagation across multiple switches
* Simple yet sufficient for analysis

---

## 🧠 4. Controller Implementation

The controller is implemented using **POX** and listens to `PacketIn` events.

### Core Logic:

* Inspect incoming packets
* Identify broadcast traffic
* Drop unnecessary broadcast packets
* Forward valid traffic

---

## 🔀 5. Flow Rule Management

Flow rules follow **match–action paradigm**:

| Match Condition | Action          |
| --------------- | --------------- |
| Broadcast MAC   | Drop packet     |
| Unicast traffic | Forward (FLOOD) |

### Behavior:

* Reduces unnecessary flooding
* Improves network control

---

## ⚙️ 6. Functionality Implementation

### ✅ Scenario 1: Normal Network

* Controller: `forwarding.l2_learning`
* Behavior: Standard switching

**Result:**

```
0% packet loss (successful communication)
```

---

### ❌ Scenario 2: Broadcast Control Enabled

* Controller: `broadcast_control`
* Behavior: Broadcast packets dropped

**Result:**

```
100% packet loss
```

### 🧠 Explanation:

ARP (Address Resolution Protocol) uses broadcast.
Blocking broadcast prevents MAC resolution → communication fails.

---

## 📊 7. Performance Evaluation

### 📌 Metrics Observed

| Metric             | Normal | Controlled       |
| ------------------ | ------ | ---------------- |
| Latency (ping)     | Low    | No communication |
| Throughput (iperf) | Normal | Reduced          |
| Broadcast traffic  | High   | Controlled       |

### 📈 Observation:

* Broadcast control reduces unnecessary traffic
* Demonstrates effectiveness of SDN-based filtering

---

## 🧪 8. Execution Steps

### Step 1: Run POX Controller

```
cd pox
./pox.py forwarding.broadcast_control
```

### Step 2: Start Mininet

```
sudo mn --controller=remote,ip=127.0.0.1 --topo linear,2
```

### Step 3: Test Connectivity

```
pingall
```
-

## 📸 10. Screenshots (Add Here)

### 🔹 Normal Network (Ping Success)

![Normal Ping](screenshots/ping_normal.png)

### 🔹 Controlled Network (Ping Failure)

![Blocked Ping](screenshots/ping_blocked.png)



---

## 🎯 11. Key Insights

* SDN enables **centralized control over traffic behavior**
* Broadcast traffic can be **selectively managed**
* Even simple logic significantly impacts network behavior

---

## 🔚 12. Conclusion

This project demonstrates how SDN can be leveraged to:

* Control broadcast traffic
* Improve network efficiency
* Enable intelligent traffic management

The implementation highlights the power of **controller-driven networking** over traditional approaches.
