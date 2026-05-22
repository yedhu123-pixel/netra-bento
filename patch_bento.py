#!/usr/bin/env python3
"""Patch Bento.html: Task 1 (card-3 IDs + JS), Task 2 (card-4 IDs), Task 3 (card-4 overlays/CSS/JS)."""

import sys

FILE = "/Users/yedhukrishnan/Downloads/Claude Code/Netra/Bento.html"

with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

warnings = []

def rep(old, new, label):
    global html
    if old not in html:
        warnings.append(f"WARN: not found — {label}")
        return
    html = html.replace(old, new, 1)
    print(f"OK: {label}")

# ══════════════════════════════════════════════════════════════
# TASK 1a — Add IDs to 6 node-inner line rects
# ══════════════════════════════════════════════════════════════

rep(
    'x="1086.37" y="182.019" width="40.6963" height="2.5" rx="1.25" fill="#ADADAD"',
    'id="c3-top-l1" x="1086.37" y="182.019" width="40.6963" height="2.5" rx="1.25" fill="#ADADAD"',
    "1a: add id c3-top-l1"
)
rep(
    'x="1086.37" y="188.519" width="19.4756" height="2.5" rx="1.25" fill="#ADADAD"',
    'id="c3-top-l2" x="1086.37" y="188.519" width="19.4756" height="2.5" rx="1.25" fill="#ADADAD"',
    "1a: add id c3-top-l2"
)
rep(
    'x="1086.43" y="317.075" width="40.6963" height="2.5" rx="1.25" fill="#ADADAD"',
    'id="c3-bot-l1" x="1086.43" y="317.075" width="40.6963" height="2.5" rx="1.25" fill="#ADADAD"',
    "1a: add id c3-bot-l1"
)
rep(
    'x="1086.43" y="323.575" width="19.4756" height="2.5" rx="1.25" fill="#ADADAD"',
    'id="c3-bot-l2" x="1086.43" y="323.575" width="19.4756" height="2.5" rx="1.25" fill="#ADADAD"',
    "1a: add id c3-bot-l2"
)
rep(
    'x="1025.42" y="249.279" width="40.6963" height="2.5" rx="1.25" fill="#ADADAD"',
    'id="c3-mid-l1" x="1025.42" y="249.279" width="40.6963" height="2.5" rx="1.25" fill="#ADADAD"',
    "1a: add id c3-mid-l1"
)
rep(
    'x="1025.42" y="255.779" width="19.4756" height="2.5" rx="1.25" fill="#ADADAD"',
    'id="c3-mid-l2" x="1025.42" y="255.779" width="19.4756" height="2.5" rx="1.25" fill="#ADADAD"',
    "1a: add id c3-mid-l2"
)

# ── Second pass: set initial width=0 ──────────────────────────
rep(
    'id="c3-top-l1" x="1086.37" y="182.019" width="40.6963"',
    'id="c3-top-l1" x="1086.37" y="182.019" width="0"',
    "1a: set width=0 c3-top-l1"
)
rep(
    'id="c3-top-l2" x="1086.37" y="188.519" width="19.4756"',
    'id="c3-top-l2" x="1086.37" y="188.519" width="0"',
    "1a: set width=0 c3-top-l2"
)
rep(
    'id="c3-bot-l1" x="1086.43" y="317.075" width="40.6963"',
    'id="c3-bot-l1" x="1086.43" y="317.075" width="0"',
    "1a: set width=0 c3-bot-l1"
)
rep(
    'id="c3-bot-l2" x="1086.43" y="323.575" width="19.4756"',
    'id="c3-bot-l2" x="1086.43" y="323.575" width="0"',
    "1a: set width=0 c3-bot-l2"
)
rep(
    'id="c3-mid-l1" x="1025.42" y="249.279" width="40.6963"',
    'id="c3-mid-l1" x="1025.42" y="249.279" width="0"',
    "1a: set width=0 c3-mid-l1"
)
rep(
    'id="c3-mid-l2" x="1025.42" y="255.779" width="19.4756"',
    'id="c3-mid-l2" x="1025.42" y="255.779" width="0"',
    "1a: set width=0 c3-mid-l2"
)

# ══════════════════════════════════════════════════════════════
# TASK 1b — Replace entire initCard3Animations JS function
# ══════════════════════════════════════════════════════════════

OLD_CARD3_JS_START = '    function initCard3Animations() {'
OLD_CARD3_JS_END   = '    setTimeout(initCard3Animations, 150);'

start_idx = html.find(OLD_CARD3_JS_START)
end_idx   = html.find(OLD_CARD3_JS_END)
if start_idx == -1 or end_idx == -1:
    warnings.append("WARN: could not find initCard3Animations block boundaries")
else:
    end_idx += len(OLD_CARD3_JS_END)
    old_block = html[start_idx:end_idx]

    NEW_CARD3_JS = r"""    function initCard3Animations() {
      var CX = 1184.48, CY = 253.779;

      // ── 1. DARK CONNECTOR PATHS DRAW (robot ↔ nodes) ─────────
      var connIds = ['c3-conn-top','c3-conn-mid','c3-conn-bot'];
      connIds.forEach(function(id) {
        var el = document.getElementById(id);
        if (!el) return;
        var len = el.getTotalLength ? el.getTotalLength() : 300;
        el.style.strokeDasharray = len + ' ' + len;
        el.style.strokeDashoffset = len;
        setTimeout(function() {
          el.style.transition = 'stroke-dashoffset 0.9s cubic-bezier(0.4,0,0.2,1)';
          el.style.strokeDashoffset = '0';
        }, 700);
      });

      // ── 2. PHASE 1: USER → BOT ───────────────────────────────
      var userToBot = [
        { userId:'c3-user-top', connId:'c3-conn-top-c', nodeId:'c3-node-top',
          lines:['c3-top-l1','c3-top-l2'], lineWidths:[40.6963,19.4756],
          particlePath:'c3-conn-top', color:'#F19B31', pulseAt:1400, lineAt:1900, nodeAt:2300 },
        { userId:'c3-user-mid', connId:'c3-conn-mid-c', nodeId:'c3-node-mid',
          lines:['c3-mid-l1','c3-mid-l2'], lineWidths:[40.6963,19.4756],
          particlePath:'c3-conn-mid', color:'#D0595A', pulseAt:2700, lineAt:3200, nodeAt:3600 },
        { userId:'c3-user-bot', connId:'c3-conn-bot-c', nodeId:'c3-node-bot',
          lines:['c3-bot-l1','c3-bot-l2'], lineWidths:[40.6963,19.4756],
          particlePath:'c3-conn-bot', color:'#FFD23F', pulseAt:4000, lineAt:4500, nodeAt:4900 }
      ];

      userToBot.forEach(function(s) {
        // 2a. User pulse
        setTimeout(function() {
          var el = document.getElementById(s.userId);
          if (!el) return;
          var bbox = el.getBBox ? el.getBBox() : null;
          if (bbox) el.style.transformOrigin = (bbox.x+bbox.width/2)+'px '+(bbox.y+bbox.height/2)+'px';
          el.style.transition = 'filter 0.5s ease-out, transform 0.5s cubic-bezier(0.34,1.56,0.64,1)';
          el.style.filter = 'drop-shadow(0 0 10px '+s.color+') drop-shadow(0 0 22px '+s.color+')';
          el.style.transform = 'scale(1.1)';
          setTimeout(function() {
            el.style.transition = 'filter 0.6s ease-in, transform 0.6s ease-in';
            el.style.filter = ''; el.style.transform = 'scale(1)';
          }, 500);
        }, s.pulseAt);

        // 2b. Colored connector line draws from node toward robot
        setTimeout(function() {
          var el = document.getElementById(s.connId);
          if (!el) return;
          var len = el.getTotalLength ? el.getTotalLength() : 80;
          el.style.strokeDasharray = len+' '+len;
          el.style.strokeDashoffset = len;
          el.style.transition = 'stroke-dashoffset 0.55s cubic-bezier(0.4,0,0.2,1)';
          el.style.strokeDashoffset = '0';
        }, s.lineAt);

        // 2c. Travel particle: user → robot (reverse=true = end→start of path)
        setTimeout(function() { spawnParticle3(s.particlePath, s.color, 1100, true); }, s.lineAt+100);

        // 2d. Node slides in from left
        setTimeout(function() {
          var el = document.getElementById(s.nodeId);
          if (!el) return;
          el.style.animation = 'c3-node-in 0.7s cubic-bezier(0.22,1,0.36,1) both';
        }, s.nodeAt);

        // 2e. Inner lines type-in after node settles
        setTimeout(function() {
          s.lines.forEach(function(lid, i) {
            var el = document.getElementById(lid);
            if (!el) return;
            var target = s.lineWidths[i];
            setTimeout(function() {
              var start = null, dur = 350 + i*120;
              (function step(ts) {
                if (!start) start = ts;
                var p = Math.min((ts-start)/dur, 1);
                var ease = p < 0.5 ? 2*p*p : -1+(4-2*p)*p;
                el.setAttribute('width', (ease*target).toFixed(3));
                if (p < 1) requestAnimationFrame(step);
              })(performance.now());
            }, i * 180);
          });
        }, s.nodeAt + 500);
      });

      // ── 3. ROBOT LIGHTS UP ────────────────────────────────────
      var robotGlowAt = 5800;
      setTimeout(function() {
        ['c3-robot-antenna','c3-robot-body','c3-robot-arm-l','c3-robot-arm-r'].forEach(function(id) {
          var el = document.getElementById(id);
          if (el) el.style.animation = 'c3-robot-glow 1.4s ease-out both';
        });
      }, robotGlowAt);

      // ── 4. PHASE 2: BOT → USER (response) ────────────────────
      var botToUser = [
        { userId:'c3-user-top', connId:'c3-conn-top-c', nodeId:'c3-node-top',
          particlePath:'c3-conn-top', color:'#8EDFFF', fireAt: robotGlowAt+800 },
        { userId:'c3-user-mid', connId:'c3-conn-mid-c', nodeId:'c3-node-mid',
          particlePath:'c3-conn-mid', color:'#8EDFFF', fireAt: robotGlowAt+1300 },
        { userId:'c3-user-bot', connId:'c3-conn-bot-c', nodeId:'c3-node-bot',
          particlePath:'c3-conn-bot', color:'#8EDFFF', fireAt: robotGlowAt+1800 }
      ];

      botToUser.forEach(function(s) {
        // Particle: robot → user (reverse=false = start→end of path, which goes robot→node)
        setTimeout(function() { spawnParticle3(s.particlePath, s.color, 1100, false); }, s.fireAt);
        // Node pulses to indicate response received
        setTimeout(function() {
          var el = document.getElementById(s.nodeId);
          if (!el) return;
          el.style.transition = 'filter 0.4s ease-out';
          el.style.filter = 'drop-shadow(0 0 8px '+s.color+') drop-shadow(0 0 20px rgba(142,223,255,0.4))';
          setTimeout(function() {
            el.style.transition = 'filter 0.6s ease-in';
            el.style.filter = '';
          }, 500);
        }, s.fireAt + 900);
        // User icon receives response glow
        setTimeout(function() {
          var el = document.getElementById(s.userId);
          if (!el) return;
          el.style.transition = 'filter 0.5s ease-out, transform 0.3s ease-out';
          el.style.filter = 'drop-shadow(0 0 8px #8EDFFF)';
          el.style.transform = 'scale(1.06)';
          setTimeout(function() {
            el.style.transition = 'filter 0.8s ease-in, transform 0.5s ease-in';
            el.style.filter = ''; el.style.transform = '';
          }, 600);
        }, s.fireAt + 1100);
      });

      // ── 5. ROBOT EYE BLINK ────────────────────────────────────
      setTimeout(function() {
        ['c3-robot-eye-l','c3-robot-eye-r'].forEach(function(id) {
          var el = document.getElementById(id);
          if (el) el.style.animation = 'c3-blink 0.35s ease-in-out 1';
        });
      }, robotGlowAt + 400);

      // ── 6. CONTINUOUS PARTICLES along connectors ──────────────
      setTimeout(function() {
        var pairs = [
          {id:'c3-conn-top', color:'#F19B31'},
          {id:'c3-conn-mid', color:'#D0595A'},
          {id:'c3-conn-bot', color:'#FFD23F'}
        ];
        pairs.forEach(function(p, i) {
          (function loop(dir) {
            spawnParticle3(p.id, i===1?'#8EDFFF':p.color, 900+i*150, dir);
            setTimeout(function(){ loop(!dir); }, 1400 + i*250);
          })(true);
        });
      }, robotGlowAt + 2600);

      // ── HELPER ────────────────────────────────────────────────
      function spawnParticle3(pathId, color, dur, reverse) {
        var path = document.getElementById(pathId);
        var container = document.getElementById('c3-particles');
        if (!path || !container) return;
        var len = path.getTotalLength ? path.getTotalLength() : 200;
        var dot = document.createElementNS('http://www.w3.org/2000/svg','circle');
        dot.setAttribute('r','2.2'); dot.setAttribute('fill',color); dot.setAttribute('opacity','0');
        container.appendChild(dot);
        var start = null;
        (function step(ts) {
          if (!start) start = ts;
          var p = Math.min((ts-start)/dur, 1);
          var t = reverse ? (1-p) : p;
          var pt = path.getPointAtLength(t*len);
          dot.setAttribute('cx', pt.x.toFixed(2));
          dot.setAttribute('cy', pt.y.toFixed(2));
          var fade = p<0.1 ? p*10 : p>0.85 ? (1-p)/0.15 : 1;
          dot.setAttribute('opacity', (fade*0.9).toFixed(2));
          if (p < 1) requestAnimationFrame(step);
          else { if(container.contains(dot)) container.removeChild(dot); }
        })(performance.now());
      }
    }

    setTimeout(initCard3Animations, 150);"""

    html = html[:start_idx] + NEW_CARD3_JS + html[end_idx:]
    print("OK: 1b: replaced initCard3Animations block")

# ══════════════════════════════════════════════════════════════
# TASK 2 — Card-4: Add IDs to elements
# ══════════════════════════════════════════════════════════════

# Panel filter groups (use data-figma-bg-blur-radius context)
rep(
    '<g filter="url(#filter27_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    '<g id="c4-panel1" filter="url(#filter27_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    "2: add id c4-panel1"
)
rep(
    '<g filter="url(#filter28_dn_29_1960)" data-figma-bg-blur-radius="51.5883">',
    '<g id="c4-panel2" filter="url(#filter28_dn_29_1960)" data-figma-bg-blur-radius="51.5883">',
    "2: add id c4-panel2"
)
rep(
    '<g filter="url(#filter29_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    '<g id="c4-panel3" filter="url(#filter29_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    "2: add id c4-panel3"
)

# Dots
rep(
    'cx="185.944" cy="591.529" r="2.61039" fill="#FB4C4E"',
    'id="c4-dot1" cx="185.944" cy="591.529" r="2.61039" fill="#FB4C4E"',
    "2: add id c4-dot1"
)
rep(
    'cx="361.944" cy="591.529" r="2.61039" fill="#FFD23F"',
    'id="c4-dot2" cx="361.944" cy="591.529" r="2.61039" fill="#FFD23F"',
    "2: add id c4-dot2"
)
rep(
    'cx="537.61" cy="591.529" r="2.61039" fill="#49DE80"',
    'id="c4-dot3" cx="537.61" cy="591.529" r="2.61039" fill="#49DE80"',
    "2: add id c4-dot3"
)

# Panel borders
rep(
    'd="M177.015 576.855H330.652C334.438 576.855 337.507 579.924 337.507',
    'id="c4-p1-border" d="M177.015 576.855H330.652C334.438 576.855 337.507 579.924 337.507',
    "2: add id c4-p1-border"
)
rep(
    'd="M353.015 576.855H506.319C510.105 576.855 513.174 579.924 513.174',
    'id="c4-p2-border" d="M353.015 576.855H506.319C510.105 576.855 513.174 579.924 513.174',
    "2: add id c4-p2-border"
)
rep(
    'd="M528.682 576.855H681.985C685.771 576.855 688.841 579.924 688.841',
    'id="c4-p3-border" d="M528.682 576.855H681.985C685.771 576.855 688.841 579.924 688.841',
    "2: add id c4-p3-border"
)

# Count number paths
rep(
    'd="M320.84 587.519C321.272 587.519 321.647 587.591',
    'id="c4-p1-count" d="M320.84 587.519C321.272 587.519 321.647 587.591',
    "2: add id c4-p1-count"
)
rep(
    'd="M491.479 587.519C491.935 587.519 492.325 587.6',
    'id="c4-p2-count" d="M491.479 587.519C491.935 587.519 492.325 587.6',
    "2: add id c4-p2-count"
)
rep(
    'd="M669.621 592.838V593.918H665.571V592.838H667.074',
    'id="c4-p3-count" d="M669.621 592.838V593.918H665.571V592.838H667.074',
    "2: add id c4-p3-count"
)

# Label paths
rep(
    'd="M199.729 594.529H198.766L198.622 591.505',
    'id="c4-p1-label" d="M199.729 594.529H198.766L198.622 591.505',
    "2: add id c4-p1-label"
)
rep(
    'd="M375.495 592.774C375.495 593.146 375.399 593.473',
    'id="c4-p2-label" d="M375.495 592.774C375.495 593.146 375.399 593.473',
    "2: add id c4-p2-label"
)
rep(
    'd="M549.083 594.646C548.279 594.646 547.655 594.373',
    'id="c4-p3-label" d="M549.083 594.646C548.279 594.646 547.655 594.373',
    "2: add id c4-p3-label"
)

# List-row groups
rep(
    '<g opacity="0.4">\n<rect opacity="0.2" x="187.072" y="618.681"',
    '<g id="c4-rows1" opacity="0.4">\n<rect opacity="0.2" x="187.072" y="618.681"',
    "2: add id c4-rows1"
)
rep(
    '<g opacity="0.4">\n<rect opacity="0.2" x="364.167" y="618.681"',
    '<g id="c4-rows2" opacity="0.4">\n<rect opacity="0.2" x="364.167" y="618.681"',
    "2: add id c4-rows2"
)
rep(
    '<g opacity="0.4">\n<rect opacity="0.2" x="539.833" y="618.681"',
    '<g id="c4-rows3" opacity="0.4">\n<rect opacity="0.2" x="539.833" y="618.681"',
    "2: add id c4-rows3"
)

# ══════════════════════════════════════════════════════════════
# TASK 3a — Insert SVG overlays after card-4 border, before </g>
# ══════════════════════════════════════════════════════════════

CARD4_BORDER_RECT = '<rect x="148" y="514" width="564" height="330" stroke="#3A3A3A"/>\n</g>'

SVG_OVERLAYS = '''<!-- Card 4 overlays -->
<defs>
  <linearGradient id="c4-diag-grad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%"   stop-color="#22FF88" stop-opacity="0"/>
    <stop offset="40%"  stop-color="#22FF88" stop-opacity="0.07"/>
    <stop offset="60%"  stop-color="#22FF88" stop-opacity="0.07"/>
    <stop offset="100%" stop-color="#22FF88" stop-opacity="0"/>
  </linearGradient>
  <clipPath id="c4-clip">
    <rect x="148" y="514" width="564" height="330"/>
  </clipPath>
  <filter id="c4-glow-f" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect id="c4-diag-sweep" x="0" y="514" width="564" height="330" fill="url(#c4-diag-grad)" clip-path="url(#c4-clip)" opacity="0"/>
<!-- Scan highlight (moves over list rows) -->
<rect id="c4-scan1" x="169.833" y="618" width="168" height="7" rx="2" fill="#ffffff" opacity="0" clip-path="url(#c4-clip)"/>
<rect id="c4-scan2" x="345.833" y="618" width="168" height="7" rx="2" fill="#ffffff" opacity="0" clip-path="url(#c4-clip)"/>
<rect id="c4-scan3" x="521.5"   y="618" width="168" height="7" rx="2" fill="#ffffff" opacity="0" clip-path="url(#c4-clip)"/>
</g>'''

rep(
    CARD4_BORDER_RECT,
    '<rect x="148" y="514" width="564" height="330" stroke="#3A3A3A"/>\n' + SVG_OVERLAYS,
    "3a: insert card-4 SVG overlays"
)

# ══════════════════════════════════════════════════════════════
# TASK 3b — Add CSS before </style>
# ══════════════════════════════════════════════════════════════

CARD4_CSS = """/* ============================================
   CARD 4 — INSIGHT DASHBOARD ANIMATIONS
============================================ */

/* Panel glow borders */
@keyframes c4-p1-glow {
  0%,100% { filter: none; }
  50%      { filter: drop-shadow(0 0 6px #FB4C4E) drop-shadow(0 0 14px rgba(251,76,78,0.35)); }
}
@keyframes c4-p2-glow {
  0%,100% { filter: none; }
  50%      { filter: drop-shadow(0 0 6px #FFD23F) drop-shadow(0 0 14px rgba(255,210,63,0.35)); }
}
@keyframes c4-p3-glow {
  0%,100% { filter: none; }
  50%      { filter: drop-shadow(0 0 6px #49DE80) drop-shadow(0 0 14px rgba(73,222,128,0.35)); }
}

/* Count flicker (simulates ticking up) */
@keyframes c4-count-tick {
  0%         { opacity: 0; }
  10%,30%,50%,70%,90% { opacity: 0.15; }
  20%,40%,60%,80%     { opacity: 0.55; }
  100%       { opacity: 1; }
}

/* Panel and element initial states */
#c4-panel1, #c4-panel2, #c4-panel3 { opacity: 0; }
#c4-p1-count, #c4-p2-count, #c4-p3-count { opacity: 0; }
#c4-p1-label, #c4-p2-label, #c4-p3-label { opacity: 0; }
#c4-dot1, #c4-dot2, #c4-dot3 { opacity: 0; }
#c4-rows1, #c4-rows2, #c4-rows3 { opacity: 0; }
"""

rep(
    '</style>',
    CARD4_CSS + '</style>',
    "3b: add card-4 CSS"
)

# ══════════════════════════════════════════════════════════════
# TASK 3c — Insert Card-4 JS before last })();
# ══════════════════════════════════════════════════════════════

CARD4_JS = r"""    // ═══════════════════════════════════════════════════════════
    // CARD 4 — INSIGHT DASHBOARD
    // ═══════════════════════════════════════════════════════════
    function initCard4Animations() {

      // ── 1. DIAGONAL GREEN GLOW SWEEP ─────────────────────────
      setTimeout(function() {
        var sweep = document.getElementById('c4-diag-sweep');
        if (!sweep) return;
        var start = null, dur = 2200;
        sweep.setAttribute('opacity','0');
        (function step(ts) {
          if (!start) start = ts;
          var p = Math.min((ts-start)/dur, 1);
          var x = -564 + p * 1128; // sweep left to right, extra wide
          var fade = p < 0.12 ? p/0.12 : p > 0.88 ? (1-p)/0.12 : 1;
          sweep.setAttribute('transform', 'translate('+x.toFixed(1)+' 0)');
          sweep.setAttribute('opacity', (fade * 0.9).toFixed(2));
          if (p < 1) requestAnimationFrame(step);
          else sweep.setAttribute('opacity','0');
        })(performance.now());
      }, 800);

      // ── 2. PANELS FADE IN LEFT → RIGHT ───────────────────────
      var panels = [
        { panelId:'c4-panel1', dotId:'c4-dot1', labelId:'c4-p1-label',
          countId:'c4-p1-count', rowsId:'c4-rows1', borderId:'c4-p1-border',
          scanId:'c4-scan1', countTarget:3,  borderAnim:'c4-p1-glow', color:'#FB4C4E',
          panelAt:1600, dotAt:2000, countAt:2300, rowsAt:2700 },
        { panelId:'c4-panel2', dotId:'c4-dot2', labelId:'c4-p2-label',
          countId:'c4-p2-count', rowsId:'c4-rows2', borderId:'c4-p2-border',
          scanId:'c4-scan2', countTarget:20, borderAnim:'c4-p2-glow', color:'#FFD23F',
          panelAt:2100, dotAt:2500, countAt:2800, rowsAt:3200 },
        { panelId:'c4-panel3', dotId:'c4-dot3', labelId:'c4-p3-label',
          countId:'c4-p3-count', rowsId:'c4-rows3', borderId:'c4-p3-border',
          scanId:'c4-scan3', countTarget:18, borderAnim:'c4-p3-glow', color:'#49DE80',
          panelAt:2600, dotAt:3000, countAt:3300, rowsAt:3700 }
      ];

      panels.forEach(function(p) {
        // Panel fade in
        setTimeout(function() {
          var el = document.getElementById(p.panelId);
          if (el) { el.style.transition = 'opacity 0.55s ease-out'; el.style.opacity = '1'; }
        }, p.panelAt);

        // Dot + label appear
        setTimeout(function() {
          [p.dotId, p.labelId].forEach(function(id) {
            var el = document.getElementById(id);
            if (el) { el.style.transition = 'opacity 0.4s ease-out'; el.style.opacity = '1'; }
          });
          // Border glow
          var border = document.getElementById(p.borderId);
          if (border) {
            border.style.animation = p.borderAnim + ' 1.2s ease-in-out 1';
          }
        }, p.dotAt);

        // Count flicker + reveal
        setTimeout(function() {
          var el = document.getElementById(p.countId);
          if (!el) return;
          el.style.animation = 'c4-count-tick 0.6s ease-out both';
        }, p.countAt);

        // Rows reveal line by line
        setTimeout(function() {
          var rows = document.getElementById(p.rowsId);
          if (!rows) return;
          rows.style.opacity = '1';
          var children = rows.children;
          // Children come in pairs: [icon, text] × 5 rows = 10 elements
          for (var i = 0; i < children.length; i++) {
            (function(el, delay) {
              el.style.opacity = '0';
              setTimeout(function() {
                el.style.transition = 'opacity 0.3s ease-out';
                el.style.opacity = String(parseFloat(el.getAttribute('opacity') || 0.2));
              }, delay);
            })(children[i], Math.floor(i/2) * 200 + (i%2)*80);
          }
        }, p.rowsAt);

        // Scanning highlight passes over rows
        setTimeout(function() {
          var scan = document.getElementById(p.scanId);
          if (!scan) return;
          var rowY = [618, 632, 646, 660, 674];
          var rowIdx = 0;
          function nextRow() {
            if (rowIdx >= rowY.length) {
              scan.setAttribute('opacity','0');
              return;
            }
            scan.setAttribute('y', rowY[rowIdx]);
            scan.setAttribute('opacity','0');
            var start = null, dur = 300;
            (function step(ts) {
              if (!start) start = ts;
              var prog = Math.min((ts-start)/dur, 1);
              var fade = prog < 0.3 ? prog/0.3 : prog > 0.7 ? (1-prog)/0.3 : 1;
              scan.setAttribute('opacity', (fade * 0.06).toFixed(3));
              if (prog < 1) requestAnimationFrame(step);
              else { rowIdx++; setTimeout(nextRow, 120); }
            })(performance.now());
          }
          setTimeout(nextRow, 100);
        }, p.rowsAt + 200);
      });
    }

    setTimeout(initCard4Animations, 200);
"""

# Find the LAST })(); in the file
last_iife = html.rfind('\n})();')
if last_iife == -1:
    warnings.append("WARN: could not find last })(); for card-4 JS insertion")
else:
    html = html[:last_iife] + '\n' + CARD4_JS + html[last_iife:]
    print("OK: 3c: inserted initCard4Animations JS before last })();")

# ══════════════════════════════════════════════════════════════
# WRITE BACK
# ══════════════════════════════════════════════════════════════
with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("\n--- DONE ---")
if warnings:
    for w in warnings:
        print(w)
else:
    print("All replacements applied successfully.")
