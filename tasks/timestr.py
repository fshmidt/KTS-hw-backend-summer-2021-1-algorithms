__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:

    if seconds < 60:
        return ('%02d' % (seconds) + "s")
    elif seconds < 3600:
        return ('%02d' % (seconds // 60)+ "m"+ '%02d' % (seconds % 60) + "s")
    elif seconds < 86400:
        return ('%02d' % (seconds // 3600)+ "h"+ '%02d' % (seconds % 3600 // 60)+ "m"+ '%02d' % (seconds % 60)+ "s")
    else:
        return('%02d' % (seconds // 86400)+ "d"+ '%02d' % (seconds % 86400 // 3600)+ "h"+ '%02d' % (seconds % 3600 // 60)+ "m"+ '%02d' % (seconds % 60)+ "s")
