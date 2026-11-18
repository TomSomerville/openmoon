Add-Type -AssemblyName System.Drawing
$dir = "C:\Users\Beached\Desktop\OpenMoon base terrain"
$src = [System.Drawing.Bitmap]::FromFile("$dir\render_towers.png")
$bmp = New-Object System.Drawing.Bitmap $src.Width, $src.Height
$g = [System.Drawing.Graphics]::FromImage($bmp); $g.DrawImage($src, 0, 0, $src.Width, $src.Height); $src.Dispose()
$g.SmoothingMode = 'AntiAlias'; $g.TextRenderingHint = 'AntiAliasGridFit'
$font = New-Object System.Drawing.Font 'Segoe UI', 20, ([System.Drawing.FontStyle]::Bold)
$orange = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(255, 255, 140, 30))
$cyan = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(255, 0, 220, 255))
$white = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::White)
$shadow = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(200, 0, 0, 0))
$pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::White), 2
# x, y (pixel of the tower foot, from Blender's projection), label parts, label offset
$items = @(
  @(594, 345, @(@('B4', $orange), @(' + M3', $cyan)), -60, -52),
  @(1078, 513, @(@('B1', $orange), @(' + M1', $cyan)), -60, -52),
  @(1298, 545, @(@('B2', $orange), @(' + M2', $cyan)), -60, -52),
  @(892, 825, @(,@('Base', $white)), -30, -52),
  @(1082, 1009, @(,@('B3', $orange)), 22, -40)
)
foreach ($it in $items) {
  $x = $it[0]; $y = $it[1]
  $g.DrawEllipse($pen, $x - 12, $y - 12, 24, 24)
  $tx = $x + $it[3]; $ty = $y + $it[4]
  foreach ($p in $it[2]) {
    $g.DrawString($p[0], $font, $shadow, $tx + 2, $ty + 2)
    $g.DrawString($p[0], $font, $p[1], $tx, $ty)
    $tx += $g.MeasureString($p[0], $font).Width - 8
  }
}
$bmp.Save("$dir\render_towers_labelled.png", [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $bmp.Dispose()
