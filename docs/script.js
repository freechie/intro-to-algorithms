const themeToggle = document.getElementById("theme-toggle");
const themes = ["auto", "light", "dark"];
const labels = { auto: "Theme", light: "Light", dark: "Dark" };

function readTheme() {
  try {
    const stored = localStorage.getItem("theme");
    return themes.includes(stored) ? stored : "auto";
  } catch {
    return "auto";
  }
}

function applyTheme(theme) {
  const root = document.documentElement;
  if (theme === "auto") {
    root.removeAttribute("data-theme");
  } else {
    root.setAttribute("data-theme", theme);
  }

  if (themeToggle) {
    const next = themes[(themes.indexOf(theme) + 1) % themes.length];
    themeToggle.textContent = labels[theme];
    themeToggle.setAttribute(
      "aria-label",
      `Theme: ${labels[theme]}. Activate to switch to ${labels[next]}.`
    );
  }

  try {
    localStorage.setItem("theme", theme);
  } catch {
    // The page still works if storage is blocked.
  }
}

applyTheme(readTheme());

themeToggle?.addEventListener("click", () => {
  const current = readTheme();
  applyTheme(themes[(themes.indexOf(current) + 1) % themes.length]);
});
