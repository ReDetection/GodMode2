from flask import redirect

from base.view import BaseView
from common.acl import ACL


class BaseDeleteView(BaseView):
    title = "Delete"
    name = "delete"
    acl = ACL.ADMIN

    def get(self, id):
        self.model.delete(id=id)
        return redirect("{}{}".format(self.model.url_prefix, self.model.name))
