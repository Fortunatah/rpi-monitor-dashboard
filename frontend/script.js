// CHANGE THIS TO YOUR PI'S IP OR HOSTNAME
const API_BASE = "http://<pi-ip>:8000";

async function fetchMetrics() {
  const statusEl = document.getElementById("status");
  try {
    const res = await fetch(`${API_BASE}/api/metrics/latest`);
    if (!res.ok) throw new Error("Network response was not ok");
    const data = await res.json();

    document.getElementById("cpu").textContent = data.cpu_percent.toFixed(1) + "%";
    document.getElementById("ram").textContent =
      `${data.ram_percent.toFixed(1)}% (${data.ram_used_mb} / ${data.ram_total_mb} MB)`;
    document.getElementById("disk").textContent =
      `${data.disk_percent.toFixed(1)}% (${data.disk_used_gb} / ${data.disk_total_gb} GB)`;

    document.getElementById("net").textContent =
      `${data.net_bytes_sent_mb} MB sent / ${data.net_bytes_recv_mb} MB recv`;

    if (data.temperature_c !== null) {
      document.getElementById("temp").textContent =
        data.temperature_c.toFixed(1) + " °C";
    } else {
      document.getElementById("temp").textContent = "N/A";
    }

    // uptime in h:m:s
    const uptime = data.uptime_seconds;
    const hours = Math.floor(uptime / 3600);
    const mins = Math.floor((uptime % 3600) / 60);
    const secs = uptime % 60;
    document.getElementById("uptime").textContent =
      `${hours}h ${mins}m ${secs}s`;

    document.getElementById("timestamp").textContent =
      `Last update: ${data.timestamp}`;
    statusEl.textContent = "Connected";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error fetching metrics";
  }
}

// initial load
fetchMetrics();
// refresh every 5 seconds
setInterval(fetchMetrics, 5000);
