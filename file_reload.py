

import sublime
import sublime_plugin


def log(msg):
    """
    Simple (print) logging function
    """
    settings = sublime.load_settings('FileReload.sublime-settings')
    if settings.get('debug', False):
        if callable(msg):
            msg = msg()
        print('[File Reload]: ' + str(msg))


class FileReloadReloadViewCommand(sublime_plugin.WindowCommand):
    def run(self, all=False):
        # Reload all views or current view
        if all:
            log('Reloading all views')
            views = self.window.views()
        else:
            log('Reloading current view')
            views = [self.window.active_view()]

        # Keep track of starting active views and group
        active_group = self.window.active_group()
        active_views = [self.window.active_view_in_group(g) for g in range(self.window.num_groups())]

        for view in views:
            group, index = self.window.get_view_index(view)

            file_name = view.file_name()
            if not file_name:
                log('Not reloading "%s"' % view.name())
                continue

            log('Reloading "%s"' % file_name)

            is_active_view = False
            if view in active_views:
                is_active_view = True
                del active_views[active_views.index(view)]

            sel = view.sel()
            if sel:
                location = ''.join([':%d' % (x + 1) for x in view.rowcol(sel[0].begin())])
                file_name += location

            self.window.focus_view(view)
            self.window.run_command('close')
            self.window.open_file(file_name, sublime.ENCODED_POSITION)
            view = self.window.active_view()
            self.window.set_view_index(view, group, index)

            if is_active_view:
                active_views.append(view)

        for view in active_views:
            self.window.focus_view(view)
        self.window.focus_group(active_group)
