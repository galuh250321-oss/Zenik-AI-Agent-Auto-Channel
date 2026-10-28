import { useState } from "react";

type View = "overview" | "channels" | "ideas" | "production" | "budget" | "settings";

type Channel = {
  id: string;
  name: string;
  language: string;
  category: string;
  duration: string;
  description: string;
  style: string;
  emoji: string;
};

const channels: Channel[] = [
  { id: "moral-id", name: "Moral & Adab", language: "Indonesia", category: "Kids", duration: "5–7 menit", description: "Cerita nilai moral, adab, dan aktivitas sehari-hari anak.", style: "2D Rigged", emoji: "🌱" },
  { id: "moral-en", name: "Good Manners & Values", language: "English", category: "Kids", duration: "5–7 min", description: "Original animated lessons in kindness, empathy, and respect.", style: "2D Rigged", emoji: "✨" },
  { id: "history-id", name: "Sejarah Nusantara", language: "Indonesia", category: "History", duration: "10–12 menit", description: "Kerajaan, tokoh, peperangan, dan sejarah peradaban.", style: "3D + Maps", emoji: "🏛️" },
  { id: "history-en", name: "Epic History", language: "English", category: "History", duration: "10–12 min", description: "Empires, strategy, civilization and historical figures.", style: "3D + Maps", emoji: "🗺️" },
];

const nav: { id: View; label: string; emoji: string }[] = [
  { id: "overview", label: "Overview", emoji: "◈" },
  { id: "channels", label: "Channel Manager", emoji: "▣" },
  { id: "ideas", label: "AI Director & Ideas", emoji: "✦" },
  { id: "production", label: "Animation Queue", emoji: "▰" },
  { id: "budget", label: "Budget Guardian", emoji: "◉" },
  { id: "settings", label: "Integrations", emoji: "⚙" },
];

const idr = (value: number) => new Intl.NumberFormat("id-ID", { style: "currency", currency: "IDR", maximumFractionDigits: 0 }).format(value);

function App() {
  const [view, setView] = useState<View>("overview");
  const [channelId, setChannelId] = useState("moral-id");
  const current = channels.find(c => c.id === channelId) ?? channels[0];
  const [budgetLimit, setBudgetLimit] = useState(4_000_000);
  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand"><div className="brand-icon">Z</div><div><strong>ZENIX</strong><small>AI STUDIO</small></div></div>
        <div className="sidebar-label">WORKSPACE</div>
        <nav aria-label="Studio sections">
          {nav.map(item => <button key={item.id} className={view === item.id ? "nav-item selected" : "nav-item"} onClick={() => setView(item.id)}>
            <span className="nav-emoji">{item.emoji}</span>{item.label}
          </button>)}
        </nav>
        <div className="sidebar-bottom">
          <span className="status-dot"></span> Phase 0 / Offline Demo
          <p>Cloud services and publishing are not connected.</p>
        </div>
      </aside>
      <main className="workspace">
        <header className="topbar">
          <div className="breadcrumbs">Zenix AI Studio <span>/</span> {nav.find(n => n.id === view)?.label}</div>
          <div className="top-actions"><span className="top-chip">Budget ceiling · {idr(budgetLimit)}</span><span className="avatar">Z</span></div>
        </header>
        <div className="content">
          <div className="eyebrow">FOUR CHANNELS · ONE AI WORKSPACE</div>
          <div className="page-head">
            <div><h1>{view === "overview" ? "Studio Overview" : nav.find(n => n.id === view)?.label}</h1>
              <p>Cloud-first animation studio · Indonesia & English · Human-approved publishing</p>
            </div>
            <span className="demo-pill">DEMO DATA ONLY</span>
          </div>
          {view === "overview" || view === "channels" ? <>
            <div className="metrics">
              <div className="metric"><span>Configured channels</span><strong>04</strong><small>2 kids · 2 history</small></div>
              <div className="metric"><span>Monthly release target</span><strong>08</strong><small>4 masters localized ×2</small></div>
              <div className="metric"><span>Monthly cap</span><strong>4M</strong><small>IDR · no payment processing</small></div>
              <div className="metric"><span>Production pipeline</span><strong>00</strong><small>Live jobs connected</small></div>
            </div>
            <section className="section-title"><div><h2>Channel workspace</h2><p>Separate topic, audience, language and publishing identity.</p></div></section>
            <div className="channel-grid">
              {channels.map(channel => <button key={channel.id} className={"channel-card " + (channel.id === channelId ? "chosen" : "")}
                onClick={() => { setChannelId(channel.id); setView("channels"); }}>
                <div className="channel-top"><span className="channel-symbol">{channel.emoji}</span><span className="category">{channel.category}</span></div>
                <h3>{channel.name}</h3><div className="subtitle">{channel.language} · {channel.duration}</div>
                <p>{channel.description}</p><div className="channel-footer"><span>{channel.style}</span><span>View details →</span></div>
              </button>)}
            </div>
            <div className="detail-panel"><div><div className="eyebrow">SELECTED CHANNEL</div><h2>{current.name}</h2>
              <p>{current.description}</p></div><div className="detail-stats"><span>{current.category.toUpperCase()}</span><strong>{current.duration}</strong><small>Publishing not connected</small></div></div>
          </> : null}
          {view === "ideas" ? <div className="placeholder-panel">
            <div className="placeholder-icon">✦</div><h2>AI Creative Director</h2>
            <p>Planned: Telegram sends research-backed proposals, synopsis, genre, references and estimated cost. Approve or revise before any paid production starts.</p>
            <div className="example"><strong>Proposal preview</strong><span>Kejujuran di Sekolah · Moral & Adab ID · 6 min</span><small>Illustration only · AI provider and Telegram not connected.</small></div>
          </div> : null}
          {view === "production" ? <div className="placeholder-panel">
            <div className="placeholder-icon">▰</div><h2>Scene-based Animation Queue</h2>
            <p>Planned: Godot rigged 2D, Blender historical sets & animated maps, FFmpeg export, selective paid AI shots, scene-level caching and preview QC.</p>
            <div className="step-row"><span>Script</span><span>Storyboard</span><span>Assets</span><span>Animate</span><span>QC</span><span>Review</span></div>
            <small>No renderer or queue service is connected yet.</small>
          </div> : null}
          {view === "budget" ? <div className="budget-screen">
            <div className="budget-hero"><div><div className="eyebrow">PLANNED SPEND CONTROL</div><h2>{idr(budgetLimit)}</h2><p>Monthly target in IDR. This slider is UI-only; it does not authorize or limit external invoices.</p></div><div className="budget-visual">0%<small>real spend tracking</small></div></div>
            <label className="slider-label" htmlFor="budgetlimit">Explore monthly target: {idr(budgetLimit)}</label>
            <input id="budgetlimit" type="range" min="2000000" max="6000000" step="250000" value={budgetLimit} onChange={e => setBudgetLimit(Number(e.target.value))}/>
            <div className="notice">Production plan: transactional ledger + channel/provider caps + pre-call reservation + fail-closed paid jobs + provider-side limits. Not implemented in Phase 0.</div>
          </div> : null}
          {view === "settings" ? <div className="integrations">
            {["Telegram Bot", "YouTube OAuth × 4", "LLM Provider Router", "Godot/Blender Render Cloud", "Cloud Database & Storage"].map(name =>
              <div key={name} className="integration"><span className="plug">◇</span><span>{name}</span><strong>NOT CONNECTED</strong></div>)}
            <p>No tokens are stored by this desktop prototype.</p>
          </div> : null}
          <footer>ZENIX AI STUDIO · Architecture prototype · No real expenditure or uploads</footer>
        </div>
      </main>
    </div>
  );
}
export default App;
