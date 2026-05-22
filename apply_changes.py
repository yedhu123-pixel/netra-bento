#!/usr/bin/env python3
"""Apply all 5 tasks to Bento.html"""

import sys

FILE = "/Users/yedhukrishnan/Downloads/Claude Code/Netra/Bento.html"

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)
warnings = []

def replace1(old, new, label):
    global content
    if old not in content:
        warnings.append(f"WARN: not found: {label}")
        return False
    content = content.replace(old, new, 1)
    print(f"OK: {label}")
    return True

# ══════════════════════════════════════════════════════════
# TASK 1a — Hide c2-particles group
# ══════════════════════════════════════════════════════════
replace1(
    '<g id="c2-particles"',
    '<g id="c2-particles" style="display:none"',
    "TASK1a c2-particles display:none"
)

# ══════════════════════════════════════════════════════════
# TASK 1b — Remove dust particle JS block
# ══════════════════════════════════════════════════════════
dust_old = '''      // ── 3. DUST PARTICLES around central icon ─────────────────
      var container = document.getElementById('c2-particles');
      if (container) {
        var cx = 711.5, cy = 247.5;
        var particles = [];
        for (var i = 0; i < 14; i++) {
          var angle = (i / 14) * Math.PI * 2 + (Math.random() - 0.5) * 0.8;
          var startR = 12 + Math.random() * 16;
          var endR   = startR + 28 + Math.random() * 24;
          var size   = 0.8 + Math.random() * 1.4;
          var delay  = 3200 + i * 180 + Math.random() * 400;
          var dur    = 2800 + Math.random() * 2000;
          particles.push({ angle: angle, startR: startR, endR: endR, size: size, delay: delay, dur: dur });
          var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          c.setAttribute('r', size);
          c.setAttribute('fill', i % 3 === 0 ? '#8EDFFF' : i % 3 === 1 ? '#2080CB' : '#ffffff');
          c.setAttribute('opacity', '0');
          c.setAttribute('cx', (cx + Math.cos(angle) * startR).toFixed(2));
          c.setAttribute('cy', (cy + Math.sin(angle) * startR).toFixed(2));
          c.dataset.particleIdx = i;
          container.appendChild(c);
        }

        function animParticle(idx) {
          var p = particles[idx];
          var c = container.children[idx];
          setTimeout(function() {
            container.style.opacity = '1';
            var start = null;
            (function step(ts) {
              if (!start) start = ts;
              var prog = Math.min((ts - start) / p.dur, 1);
              var ease = prog < 0.1 ? prog * 10 : prog > 0.7 ? (1 - prog) / 0.3 : 1;
              var r = p.startR + (p.endR - p.startR) * prog;
              c.setAttribute('cx', (cx + Math.cos(p.angle) * r).toFixed(2));
              c.setAttribute('cy', (cy + Math.sin(p.angle) * r).toFixed(2));
              c.setAttribute('opacity', (ease * 0.55).toFixed(2));
              if (prog < 1) requestAnimationFrame(step);
              else {
                c.setAttribute('cx', (cx + Math.cos(p.angle) * p.startR).toFixed(2));
                c.setAttribute('cy', (cy + Math.sin(p.angle) * p.startR).toFixed(2));
                c.setAttribute('opacity', '0');
                animParticle(idx); // loop
              }
            })(performance.now());
          }, p.delay);
        }
        particles.forEach(function(_, i) { animParticle(i); });
      }'''

dust_new = '      // dust particles removed'

replace1(dust_old, dust_new, "TASK1b dust particles JS block")

# ══════════════════════════════════════════════════════════
# TASK 2 — Add IDs to card-3 elements
# ══════════════════════════════════════════════════════════

# c3-ring-0
replace1(
    'cx="1184.48" cy="253.779" r="137.378" transform="rotate(-90 1184.48 253.779)"',
    'id="c3-ring-0" cx="1184.48" cy="253.779" r="137.378" transform="rotate(-90 1184.48 253.779)"',
    "TASK2 c3-ring-0"
)

# c3-ring-1 — use the line context: the <g filter17 is preceded by a specific rect
# Check actual context to ensure uniqueness
replace1(
    '<g filter="url(#filter17_d_29_1960)">',
    '<g id="c3-ring-1" filter="url(#filter17_d_29_1960)">',
    "TASK2 c3-ring-1"
)

replace1(
    '<g filter="url(#filter18_d_29_1960)">',
    '<g id="c3-ring-2" filter="url(#filter18_d_29_1960)">',
    "TASK2 c3-ring-2"
)

replace1(
    '<g filter="url(#filter19_d_29_1960)">',
    '<g id="c3-ring-3" filter="url(#filter19_d_29_1960)">',
    "TASK2 c3-ring-3"
)

# Robot parts
replace1(
    'd="M1184.48 246.449V239.121H1177.15"',
    'id="c3-robot-antenna" d="M1184.48 246.449V239.121H1177.15"',
    "TASK2 c3-robot-antenna"
)

replace1(
    'd="M1195.47 246.45H1173.48C1171.46 246.45',
    'id="c3-robot-body" d="M1195.47 246.45H1173.48C1171.46 246.45',
    "TASK2 c3-robot-body"
)

replace1(
    'd="M1166.15 257.443H1169.82"',
    'id="c3-robot-arm-l" d="M1166.15 257.443H1169.82"',
    "TASK2 c3-robot-arm-l"
)

replace1(
    'd="M1199.13 257.443H1202.8"',
    'id="c3-robot-arm-r" d="M1199.13 257.443H1202.8"',
    "TASK2 c3-robot-arm-r"
)

replace1(
    'd="M1189.97 255.61V259.275"',
    'id="c3-robot-eye-r" d="M1189.97 255.61V259.275"',
    "TASK2 c3-robot-eye-r"
)

replace1(
    'd="M1178.98 255.61V259.275"',
    'id="c3-robot-eye-l" d="M1178.98 255.61V259.275"',
    "TASK2 c3-robot-eye-l"
)

# Connectors
replace1(
    'd="M1144.07 253.778L1086.77 253.778" stroke="#4C4D4D"',
    'id="c3-conn-mid" d="M1144.07 253.778L1086.77 253.778" stroke="#4C4D4D"',
    "TASK2 c3-conn-mid"
)

replace1(
    'd="M1184.25 213.925V194.35C1184.25 190.025 1180.74 186.519 1176.42 186.519H1143.14"',
    'id="c3-conn-top" d="M1184.25 213.925V194.35C1184.25 190.025 1180.74 186.519 1176.42 186.519H1143.14"',
    "TASK2 c3-conn-top"
)

replace1(
    'd="M1184.25 294.169V313.744C1184.25 318.069 1180.74 321.575 1176.42 321.575H1143.14"',
    'id="c3-conn-bot" d="M1184.25 294.169V313.744C1184.25 318.069 1180.74 321.575 1176.42 321.575H1143.14"',
    "TASK2 c3-conn-bot"
)

replace1(
    'd="M1134.11 253.778L1104.11 253.778"',
    'id="c3-conn-mid-c" d="M1134.11 253.778L1104.11 253.778"',
    "TASK2 c3-conn-mid-c"
)

replace1(
    'd="M1184.25 302.169V313.575C1184.25 317.993',
    'id="c3-conn-bot-c" d="M1184.25 302.169V313.575C1184.25 317.993',
    "TASK2 c3-conn-bot-c"
)

replace1(
    'd="M1184.25 205.951V194.546C1184.25 190.127',
    'id="c3-conn-top-c" d="M1184.25 205.951V194.546C1184.25 190.127',
    "TASK2 c3-conn-top-c"
)

# User/node filter groups — need unique context
# filter20: the <g filter="url(#filter20..." is on line 552
replace1(
    '<g filter="url(#filter20_d_29_1960)">',
    '<g id="c3-user-top" filter="url(#filter20_d_29_1960)">',
    "TASK2 c3-user-top"
)

replace1(
    '<g filter="url(#filter22_d_29_1960)">',
    '<g id="c3-user-bot" filter="url(#filter22_d_29_1960)">',
    "TASK2 c3-user-bot"
)

replace1(
    '<g filter="url(#filter24_d_29_1960)">',
    '<g id="c3-user-mid" filter="url(#filter24_d_29_1960)">',
    "TASK2 c3-user-mid"
)

# filter21/23/25 _n_ groups — use surrounding foreignObject for uniqueness
replace1(
    '<g filter="url(#filter21_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    '<g id="c3-node-top" filter="url(#filter21_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    "TASK2 c3-node-top"
)

replace1(
    '<g filter="url(#filter23_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    '<g id="c3-node-bot" filter="url(#filter23_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    "TASK2 c3-node-bot"
)

replace1(
    '<g filter="url(#filter25_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    '<g id="c3-node-mid" filter="url(#filter25_n_29_1960)" data-figma-bg-blur-radius="51.5883">',
    "TASK2 c3-node-mid"
)

# Outer user circles
replace1(
    '<circle cx="1044.03" cy="186.546" r="20.1954" fill="url(#paint30_linear_29_1960)"/>',
    '<circle id="c3-user-top-outer" cx="1044.03" cy="186.546" r="20.1954" fill="url(#paint30_linear_29_1960)"/>',
    "TASK2 c3-user-top-outer"
)

replace1(
    '<circle cx="1044.21" cy="321.565" r="20.1954" fill="url(#paint33_linear_29_1960)"/>',
    '<circle id="c3-user-bot-outer" cx="1044.21" cy="321.565" r="20.1954" fill="url(#paint33_linear_29_1960)"/>',
    "TASK2 c3-user-bot-outer"
)

# ══════════════════════════════════════════════════════════
# TASK 3 — Insert SVG overlay elements after card-3 border rect
# ══════════════════════════════════════════════════════════
task3_anchor = '<rect x="922" y="108" width="370" height="389" stroke="#3A3A3A"/>'
task3_insert = '''<rect x="922" y="108" width="370" height="389" stroke="#3A3A3A"/>
<!-- Card 3 overlays -->
<defs>
  <clipPath id="c3-card-clip">
    <rect x="922" y="108" width="370" height="389"/>
  </clipPath>
  <filter id="c3-cyan-glow" x="-100%" y="-100%" width="300%" height="300%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"/>
    <feColorMatrix in="blur" type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.85  0 0 0 0 1  0 0 0 0.7 0" result="cyan"/>
    <feMerge><feMergeNode in="cyan"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="c3-user-glow" x="-150%" y="-150%" width="400%" height="400%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<!-- Travel particles container — populated by JS -->
<g id="c3-particles" clip-path="url(#c3-card-clip)" opacity="1"/>'''

replace1(task3_anchor, task3_insert, "TASK3 SVG overlay elements")

# ══════════════════════════════════════════════════════════
# TASK 4 — Add CSS animations before </style>
# ══════════════════════════════════════════════════════════
css_block = '''/* ============================================
   CARD 3 — MULTI-AGENT SIMULATION ANIMATIONS
============================================ */

/* Orbit ring rotations */
@keyframes c3-rotate-cw  { from { transform: rotate(0deg);   } to { transform: rotate(360deg);  } }
@keyframes c3-rotate-ccw { from { transform: rotate(0deg);   } to { transform: rotate(-360deg); } }

/* User icon pulse */
@keyframes c3-user-pulse {
  0%   { transform: scale(1);    filter: none; }
  40%  { transform: scale(1.12); filter: drop-shadow(0 0 8px currentColor) drop-shadow(0 0 20px currentColor); }
  100% { transform: scale(1);    filter: none; }
}

/* Message node slide-in with bounce */
@keyframes c3-node-in {
  0%   { opacity: 0; transform: translateX(-22px); }
  60%  { opacity: 1; transform: translateX(3px);   }
  80%  { transform: translateX(-1px); }
  100% { opacity: 1; transform: translateX(0);     }
}

/* Robot glow */
@keyframes c3-robot-glow {
  0%   { filter: none; }
  50%  { filter: drop-shadow(0 0 6px #8EDFFF) drop-shadow(0 0 14px rgba(142,223,255,0.5)); }
  100% { filter: drop-shadow(0 0 3px rgba(142,223,255,0.3)); }
}

/* Eye blink */
@keyframes c3-blink {
  0%, 100% { opacity: 1;   }
  40%, 60%  { opacity: 0.1; }
}

/* Apply ring rotations — all centered on robot (1184.48, 253.779) */
#c3-ring-0 {
  transform-origin: 1184.48px 253.779px;
  animation: c3-rotate-cw 28s linear 0.5s infinite;
}
#c3-ring-1 {
  transform-origin: 1184.48px 253.779px;
  animation: c3-rotate-ccw 20s linear 0.5s infinite;
}
#c3-ring-2 {
  transform-origin: 1184.48px 253.779px;
  animation: c3-rotate-cw 14s linear 0.5s infinite;
}
#c3-ring-3 {
  transform-origin: 1184.48px 253.779px;
  animation: c3-rotate-ccw 9s linear 0.5s infinite;
}

/* Node slide-ins — triggered by JS adding class or inline style */
#c3-node-top { opacity: 0; }
#c3-node-bot { opacity: 0; }
#c3-node-mid { opacity: 0; }

/* Robot and eyes — initial state for JS-driven glow */
#c3-robot-antenna, #c3-robot-body, #c3-robot-arm-l, #c3-robot-arm-r { opacity: 1; }
#c3-robot-eye-l, #c3-robot-eye-r { opacity: 1; }
'''

replace1(
    '</style>',
    css_block + '</style>',
    "TASK4 CSS animations"
)

# ══════════════════════════════════════════════════════════
# TASK 5 — Add card-3 JS before last })();
# ══════════════════════════════════════════════════════════
js_block = '''
    // ═══════════════════════════════════════════════════════════
    // CARD 3 — MULTI-AGENT SIMULATION
    // ═══════════════════════════════════════════════════════════
    function initCard3Animations() {
      var CX = 1184.48, CY = 253.779; // robot center

      // ── 1. CONNECTOR LINE DRAW (dark gray, full paths) ───────
      // Draw all three connector paths before anything else,
      // but keep them visible at low opacity so the scene reads.
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
        }, 800);
      });

      // ── 2. USER PULSE → LINE DRAW → NODE SLIDE-IN ────────────
      var sequence = [
        {
          userId: 'c3-user-top', connId: 'c3-conn-top-c',
          nodeId: 'c3-node-top', particlePath: 'c3-conn-top',
          color: '#F19B31', pulseAt: 1400, lineAt: 1900, nodeAt: 2300
        },
        {
          userId: 'c3-user-mid', connId: 'c3-conn-mid-c',
          nodeId: 'c3-node-mid', particlePath: 'c3-conn-mid',
          color: '#D0595A', pulseAt: 2600, lineAt: 3100, nodeAt: 3500
        },
        {
          userId: 'c3-user-bot', connId: 'c3-conn-bot-c',
          nodeId: 'c3-node-bot', particlePath: 'c3-conn-bot',
          color: '#FFD23F', pulseAt: 3800, lineAt: 4300, nodeAt: 4700
        }
      ];

      sequence.forEach(function(s) {
        // 2a. User pulse
        setTimeout(function() {
          var el = document.getElementById(s.userId);
          if (!el) return;
          el.style.transformOrigin = 'center';
          var bbox = el.getBBox ? el.getBBox() : null;
          if (bbox) el.style.transformOrigin = (bbox.x + bbox.width/2) + 'px ' + (bbox.y + bbox.height/2) + 'px';
          el.style.transition = 'filter 0.5s ease-out, transform 0.5s cubic-bezier(0.34,1.56,0.64,1)';
          el.style.filter = 'drop-shadow(0 0 10px ' + s.color + ') drop-shadow(0 0 22px ' + s.color + ')';
          el.style.transform = 'scale(1.12)';
          setTimeout(function() {
            el.style.transition = 'filter 0.6s ease-in, transform 0.6s ease-in';
            el.style.filter = '';
            el.style.transform = 'scale(1)';
          }, 500);
        }, s.pulseAt);

        // 2b. Colored connector line draws toward robot
        setTimeout(function() {
          var el = document.getElementById(s.connId);
          if (!el) return;
          var len = el.getTotalLength ? el.getTotalLength() : 80;
          el.style.strokeDasharray = len + ' ' + len;
          el.style.strokeDashoffset = len;
          el.style.transition = 'stroke-dashoffset 0.55s cubic-bezier(0.4,0,0.2,1)';
          el.style.strokeDashoffset = '0';
        }, s.lineAt);

        // 2c. Node slides in
        setTimeout(function() {
          var el = document.getElementById(s.nodeId);
          if (!el) return;
          el.style.animation = 'c3-node-in 0.7s cubic-bezier(0.22,1,0.36,1) both';
        }, s.nodeAt);

        // 2d. Travel particle along full connector
        setTimeout(function() {
          spawnParticle(s.particlePath, s.color, 1200, true);
        }, s.lineAt + 100);
      });

      // ── 3. ROBOT GLOW + BRACKET DRAW ─────────────────────────
      setTimeout(function() {
        // Robot cyan glow
        var robotParts = ['c3-robot-antenna','c3-robot-body','c3-robot-arm-l','c3-robot-arm-r'];
        robotParts.forEach(function(id) {
          var el = document.getElementById(id);
          if (el) el.style.animation = 'c3-robot-glow 1.2s ease-out both';
        });

        // Yellow bracket draw (top and bottom colored arcs)
        ['c3-conn-top-c','c3-conn-bot-c','c3-conn-mid-c'].forEach(function(id) {
          var el = document.getElementById(id);
          if (!el) return;
          var len = el.getTotalLength ? el.getTotalLength() : 80;
          el.style.strokeDasharray = len + ' ' + len;
          el.style.strokeDashoffset = len;
          setTimeout(function() {
            el.style.transition = 'stroke-dashoffset 0.6s cubic-bezier(0.25,0.46,0.45,0.94)';
            el.style.strokeDashoffset = '0';
          }, 50);
        });
      }, 5400);

      // ── 4. ROBOT EYE BLINK ────────────────────────────────────
      setTimeout(function() {
        ['c3-robot-eye-l','c3-robot-eye-r'].forEach(function(id) {
          var el = document.getElementById(id);
          if (el) el.style.animation = 'c3-blink 0.35s ease-in-out 1';
        });
      }, 6000);

      // ── 5. CONTINUOUS PARTICLES along all connectors ──────────
      setTimeout(function() {
        ['c3-conn-top','c3-conn-mid','c3-conn-bot'].forEach(function(id, i) {
          var colors = ['#F19B31','#D0595A','#FFD23F'];
          (function loop() {
            spawnParticle(id, colors[i], 1000 + i * 200, false);
            setTimeout(loop, 1800 + i * 300);
          })();
        });
      }, 5600);

      // ── HELPER: spawn a particle along a path ─────────────────
      function spawnParticle(pathId, color, dur, reverse) {
        var path = document.getElementById(pathId);
        var container = document.getElementById('c3-particles');
        if (!path || !container) return;
        var len = path.getTotalLength ? path.getTotalLength() : 200;
        var dot = document.createElementNS('http://www.w3.org/2000/svg','circle');
        dot.setAttribute('r','2.2');
        dot.setAttribute('fill', color);
        dot.setAttribute('opacity','0');
        container.appendChild(dot);
        var start = null;
        (function step(ts) {
          if (!start) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var t = reverse ? (1 - p) : p;
          var pt = path.getPointAtLength(t * len);
          dot.setAttribute('cx', pt.x.toFixed(2));
          dot.setAttribute('cy', pt.y.toFixed(2));
          var fade = p < 0.1 ? p * 10 : p > 0.85 ? (1 - p) / 0.15 : 1;
          dot.setAttribute('opacity', (fade * 0.9).toFixed(2));
          if (p < 1) requestAnimationFrame(step);
          else { container.removeChild(dot); }
        })(performance.now());
      }
    }

    setTimeout(initCard3Animations, 150);
'''

# Find the LAST occurrence of })(); and insert before it
last_iife_idx = content.rfind('})();')
if last_iife_idx == -1:
    warnings.append("WARN: not found: TASK5 })(); IIFE closing")
else:
    content = content[:last_iife_idx] + js_block + content[last_iife_idx:]
    print("OK: TASK5 card-3 JS inserted before last })();")

# ══════════════════════════════════════════════════════════
# Write back
# ══════════════════════════════════════════════════════════
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nFile written. Original size: {original_len}, New size: {len(content)}")

if warnings:
    print("\n--- WARNINGS ---")
    for w in warnings:
        print(w)
else:
    print("\nAll replacements successful — no warnings.")
