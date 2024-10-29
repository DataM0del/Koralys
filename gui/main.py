from gi import require_version

require_version("Gtk", "4.0")
require_version("Adw", "1")
require_version("GtkSource", "5")
from gi.repository import Gtk, Adw, GtkSource  # noqa: E402


class CodeWidget(Gtk.ScrolledWindow):
    def __init__(self):
        super().__init__(height_request=180, width_request=600, has_frame=True)
        GtkSource.init()

        # Get the language we want to use
        language_manager = GtkSource.LanguageManager.get_default()
        language = language_manager.get_language("lua")

        # Create the buffer - this holds the text that's used in the SourceView
        style_scheme_manager = GtkSource.StyleSchemeManager.get_default()
        buffer = GtkSource.Buffer.new_with_language(language)
        buffer.set_style_scheme(style_scheme_manager.get_scheme("solarized-dark"))
        buffer.set_text('print("ae")')

        # Create the SourceView which displays the buffer's display
        source_view = GtkSource.View(
            auto_indent=True,
            indent_width=4,
            buffer=buffer,
            show_line_numbers=True,
            insert_spaces_instead_of_tabs=False,
        )
        self.set_child(source_view)


class Gui(Adw.Application):
    def __init__(self):
        super().__init__()
        self.connect("activate", self.on_activate)

    def on_activate(self, _):
        win = Gtk.ApplicationWindow(application=self)
        win.set_title("Koralys")
        win.set_default_size(800, 600)
        win.present()
        tab_view = Adw.TabView.new()
        code_widget = CodeWidget()
        # icon_theme = Gtk.IconTheme.get_for_display(win.get_display())
        # icon = icon_theme.lookup_icon("code", None, 48, 1, Gtk.TextDirection.LTR, 0)
        code_page = Adw.TabPage(title="Code", child=code_widget)
        tab_view.add_page(code_widget, code_page)
        win.set_child(tab_view)

Gui().run()
