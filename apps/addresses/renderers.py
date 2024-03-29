import json

from rest_framework.renderers import JSONRenderer


class AddressJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_types=None, renderer_context=None):
        errors = data.get("errors", None)

        if errors is not None:
            return super(AddressJSONRenderer, self).render(data)

        return json.dumps({"address": data})
