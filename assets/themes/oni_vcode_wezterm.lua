-- Onichan-Baka-vcode (Oni-VCode) Animated Anime Terminal Config for WezTerm
local wezterm = require 'wezterm'
local config = wezterm.config_builder()

local wallpapers = {
  "/working_dir/c_2777cf7d1f577b18/skills/onichan-baka-vcode/assets/wallpapers/theme_1_cliff_swordsman.jpg",
  "/working_dir/c_2777cf7d1f577b18/skills/onichan-baka-vcode/assets/wallpapers/theme_2_moonlight_dualblade.jpg",
}

config.font = wezterm.font_with_fallback({
  'Anime Script',
  'JetBrains Mono',
  'Cascadia Code',
})
config.font_size = 13.5
config.window_background_opacity = 0.88
config.macos_window_background_blur = 20
config.window_background_image = wallpapers[1]
config.window_background_image_hsb = {
  brightness = 0.22,
  hue = 1.0,
  saturation = 1.15,
}

-- Auto-cycle between the 2 Anime Wallpapers every 30 seconds
wezterm.on('update-right-status', function(window, pane)
  local idx = (math.floor(os.time() / 30) % #wallpapers) + 1
  local overrides = window:get_config_overrides() or {}
  if overrides.window_background_image ~= wallpapers[idx] then
    overrides.window_background_image = wallpapers[idx]
    window:set_config_overrides(overrides)
  end
  window:set_right_status(wezterm.format({
    { Foreground = { Color = '#00f2fe' } },
    { Text = ' ⚔️ Oni-VCode [' .. idx .. '/2] ' },
  }))
end)

return config
